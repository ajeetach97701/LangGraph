


from Libs.libs import *


from Tools.availability_by_doctor import *
from Tools.availability_by_specialization import *
from Tools.booking import book_appointment

class MessagesState(TypedDict):
    messages: Annotated[List[AnyMessage], operator.add]
    senderId:str
    history:str
    
    
tools = [check_availability_by_doctor, check_availability_by_specialization, book_appointment]
# tool = [mercedes_tool]
tool_node = ToolNode(tools=tools)
model = llm.bind_tools(tools = tools, strict=True)

def read_human_feedback(state):
    # if state['messages'][-1].tool_calls == []:
    #     logger.info("AI: "+ state['messages'][-1].content)
    #     user_msg = input("Reply: ")
    
    
    # history = {"history":[]}
    history = getData("abcsdd")
    if history is None:
        history = {'history':[]}
    history_new = {"human":f"{state['messages'][0].content}", "ai":f"{state['messages'][-1].content}"}



    # history = history_new.append(history['history'])
    history['history'].append(history_new)
    print(history)

        
        
    
    # history['history'].append(history_new)
    
    setData(state['senderId'], history)
    
    if len(history['history'])>4:
        length = len(history['history']) - 4
        for i in range(length):
            history["history"].pop(0)
    
    # a = getData("abcsdd")
    # combined_history.append(a)
    # {"history":combined_history}
        
    
    
    print()
    print(state)
    print("history",history)
    print()
    return state
    #     pass

def call_model(state: MessagesState):
    
    
    
    print("From call_model the state is:",state['senderId'])
    s = getData(state["senderId"])
    state["history"] = s
    # As reference, today is {datetime.now().strftime('%Y-%m-%d %H:%M, %A')}

    # history = {"human":state["messages"][1], "AI":"This is ai response"}
    messages = [SystemMessage(content=f"You are helpful assistant.\n.\nKeep a friendly, professional tone.\nAvoid verbosity.\nConsiderations:\n- Don´t assume parameters in call functions that it didnt say.\n- MUST NOT force users how to write. Let them write in the way they want.\n- The conversation should be very natural like a secretary talking with a client.\n- Call only ONE tool at a time. You are also provided a conversation history between you and human. You also have history to answer the user queries{state['history']}. ")] + state['messages']
    # messages = [SystemMessage(content="You are a helpful assistant. As reference, today is {datetime.now().strftime('%Y-%m-%d %H:%M, %A')}. Always use tools to answer the queries")]
    print(messages)
    response = model.invoke(messages)
    return {"messages": [response]}

def should_continue(state: MessagesState) -> Literal["tools", "human"]:
    messages = state['messages']
    last_message = messages[-1]
    if last_message.tool_calls:
        return "tools"
    return "human"




def should_continue_with_feedback(state: MessagesState) -> Literal["agent", "end", "human"]:
    messages = state['messages']
    last_message = messages[-1]
    if isinstance(last_message, dict):
        if last_message.get("type","") == 'human':
            return "agent"
    if (isinstance(last_message, HumanMessage)):
        return "agent"
    if (isinstance(last_message, AIMessage)):
        return "end"
    return "end"



def graph(query:str, senderId:str):
    workflow = StateGraph(MessagesState)
    workflow.add_node("agent",call_model)
    workflow.add_node("tools",tool_node)
    workflow.add_node("human", read_human_feedback)


    workflow.add_conditional_edges(
        "agent",
        should_continue,
        {"human":"human",
        "tools":"tools"}
    )
    workflow.add_conditional_edges(
        "human",
        should_continue_with_feedback,
        {"agent":"agent","end":END}
    )

    workflow.add_edge("tools","agent" )


    workflow.set_entry_point('agent')



    graph = workflow.compile()
    inputs = {"messages":[HumanMessage(content=query)], "senderId":senderId}

    for response in graph.stream(inputs):
        try:
            if "__end__" not in response:
                token_usage =response['human']['messages'][-1].response_metadata['token_usage']
                final_response =  response['human']['messages'][-1].content
                print("-----")
                # history = {"human":query, "ai":final_response}
                return {"result": final_response, "token_usage":token_usage}
        except:
            print("error")



