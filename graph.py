from Libs.libs import *
from Tools.tools_init_ import GetCustomTools
from Tools.ragAgent import rag_tool
from Agent.supervisor_agent import supervisor_agent_make, agent_node
from models.Schema import *

# The agent state is the input to each node in the graph


def graph(request_data):
    def graph_main():
        def read_human_feedback(state):
            return state

        def should_continue(state: MessagesState) -> Literal["Rag", "Appointments"]:
            print("Inside should continue", state["next"])
            if state["next"] == "FINISH":
                return "human_feedback"
            return state["next"]

        toolsInstance = GetCustomTools(request_data)
        tools_available = toolsInstance.get_tools()

        class routeResponse(BaseModel):
            next: Literal["Appointments", "Rag", "FINISH"]

        from Tools.ragAgent import create_custom_agent

        Appointments_agnet = create_custom_agent(
            prompt="""You are an intelligent agent that answers queries related to the appointment with doctor based on doctor name, specialization, schedule appointment and reschedule appoinments.""",
            tools=tools_available,
        )
        Appointments_node = functools.partial(
            agent_node, agent=Appointments_agnet, name="Appointments"
        )

        Rag_agent = create_custom_agent(
            prompt="""You are an intelligent agent that answers queries related to TATA Punch EV vehicles and its variants.""",
            tools=[rag_tool],
        )

        Rag_node = functools.partial(agent_node, agent=Rag_agent, name="Rag")
        workflow = StateGraph(AgentState)
        workflow.add_node("Appointments", Appointments_node)
        workflow.add_node("Rag", Rag_node)
        workflow.add_node("supervisor_agent", supervisor_agent_make)
        workflow.add_node("human_feedback", read_human_feedback)

        # workflow.add_edge("Appointments", "supervisor_agent")
        conditional_map = {
            "Appointments": "Appointments",
            "Rag": "Rag",
            "FINISH": "__end__",
        }
        # workflow.add_conditional_edges("supervisor_agent", lambda x: x["next"], conditional_map)

        workflow.add_conditional_edges(
            "supervisor_agent",
            should_continue,
            {
                "Rag": "Rag",
                "Appointments": "Appointments",
                "human_feedback": "human_feedback",
            },
        )
        workflow.add_edge("human_feedback", END)

        workflow.add_edge(
            "Appointments",
            "supervisor_agent",
        )

        workflow.add_edge(
            "Rag",
            "supervisor_agent",
        )

        workflow.add_edge(START, "supervisor_agent")

        with RedisSaver.from_conn_info(
            host="localhost", port=6379, db=0
        ) as checkpointer:
            graph = workflow.compile(checkpointer=checkpointer)
            # inputs = {
            #     "messages": [HumanMessage(content=query)],
            #     "senderId": request_data.senderId,
            # }
            inputs = {
                "messages": [HumanMessage(content=request_data.query)],
            }
            config = {"configurable": {"thread_id": request_data.senderId}}

            # graph = workflow.compile(debug=True)

            # display(Image(graph.get_graph(xray=True).draw_mermaid_png()))

            for s in graph.stream(
                # {"messages": [HumanMessage(content=request_data.query)]},
                # {"recursion_limit": 100},
                inputs,
                config,
                debug=True,
            ):
                if "__end__" not in s:
                    if "human_feedback" in s:
                        mdprint(s["human_feedback"]["messages"][-1].content)
                        response = s["human_feedback"]["messages"][-1].content
                        return response
                        print()
                        print()
                        break
                    print(s)
                    print()
                    print()
                    print()
                    print("This is s.,.,.,.", s)
                    print("----")
                else:
                    print(s)

    return graph_main()
