from Libs.libs import *

from Redis.utilis import RedisSaver

from Tools.availability_by_doctor import *
from Tools.availability_by_specialization import *
from Tools.booking import book_appointment


class MessagesState(TypedDict):
    messages: Annotated[List[AnyMessage], operator.add]
    senderId: str
    history: str


from Tools.tools_init_ import *


def graph(request_data):
    print()
    print()
    print(request_data)
    print()
    print()
    toolsInstance = GetCustomTools(request_data)
    tools_available = toolsInstance.get_tools()
    # tools_available = [book_appointment,check_availability_by_doctor, check_availability_by_specialization]
    # tool = [mercedes_tool]
    tool_node = ToolNode(tools=tools_available)
    model = llm.bind_tools(tools=tools_available, strict=True)

    def read_human_feedback(state):
        return state

    def call_model(state: MessagesState):

        print()
        print()
        print("From call_model the state is:", state["messages"][-1].content)
        print()
        print()

        messages = [
            SystemMessage(
                content=f"You are helpful assistant.\n.As reference, today is {datetime.now().strftime('%Y-%m-%d %H:%M, %A')}\nKeep a friendly, professional tone.\nAvoid verbosity.\nConsiderations:\n- Don´t assume parameters in call functions that it didnt say.\n- MUST NOT force users how to write. Let them write in the way they want.\n- The conversation should be very natural like a secretary talking with a client.\n- Call only ONE tool at a time."
            )
        ] + state["messages"]
        # messages = [SystemMessage(content="You are a helpful assistant. As reference, today is {datetime.now().strftime('%Y-%m-%d %H:%M, %A')}. Always use tools to answer the queries")]

        response = model.invoke(messages)
        return {"messages": [response]}

    def should_continue(state: MessagesState) -> Literal["tools", "human_feedback"]:
        messages = state["messages"]
        last_message = messages[-1]
        if last_message.tool_calls:
            return "tools"
        return "human_feedback"

    def should_continue_with_feedback(
        state: MessagesState,
    ) -> Literal["agent", "end", "human_feedback"]:
        messages = state["messages"]
        last_message = messages[-1]
        if isinstance(last_message, dict):
            if last_message.get("type", "") == "human_feedback":
                return "agent"
        if isinstance(last_message, HumanMessage):
            return "agent"
        if isinstance(last_message, AIMessage):
            return "end"
        return "end"

    def graph_main(query: str, senderId: str):
        workflow = StateGraph(MessagesState)
        workflow.add_node("agent", call_model)
        workflow.add_node("tools", tool_node)
        workflow.add_node("human_feedback", read_human_feedback)

        workflow.add_conditional_edges(
            "agent",
            should_continue,
            {"human_feedback": "human_feedback", "tools": "tools"},
        )
        workflow.add_conditional_edges(
            "human_feedback",
            should_continue_with_feedback,
            {"agent": "agent", "end": END},
        )

        workflow.add_edge("tools", "agent")

        workflow.set_entry_point("agent")

        graph = workflow.compile()

        with RedisSaver.from_conn_info(
            host="localhost", port=6379, db=0
        ) as checkpointer:
            graph = workflow.compile(checkpointer=checkpointer)
            inputs = {"messages": [HumanMessage(content=query)], "senderId": senderId}
            config = {"configurable": {"thread_id": senderId}}

            for response in graph.stream(inputs, config):
                try:
                    if "__end__" not in response:
                        # if 'human_feedback' in response:
                        token_usage = response["human_feedback"]["messages"][
                            -1
                        ].response_metadata["token_usage"]
                        final_response = response["human_feedback"]["messages"][
                            -1
                        ].content

                        print("-----")
                        # latest_checkpoint = checkpointer.get(config)
                        latest_checkpoint_tuple = checkpointer.get_tuple(config)
                        # checkpoint_tuples = list(checkpointer.list(config))
                        # history = {"human_feedback":query, "ai":final_response}
                        return {"result": final_response, "token_usage": token_usage}
                except Exception as e:
                    print("error", e)

    return graph_main(query=request_data.query, senderId=request_data.senderId)
