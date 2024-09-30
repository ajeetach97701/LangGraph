


from langchain_core.messages import HumanMessage, SystemMessage
from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import END, StateGraph, MessagesState
from langgraph.prebuilt import ToolNode
from typing import TypedDict, Annotated, List, Literal
from langchain_core.messages import AnyMessage, HumanMessage
import operator
from Libs.libs import *
from Agent.agent_supervisor_take_2 import *
from datetime import datetime


from Libs.libs import *

class MessagesState(TypedDict):
    messages: Annotated[List[AnyMessage], operator.add]

tools = [check_availability_by_doctor, check_availability_by_specialization, book_appointment]
# tool = [mercedes_tool]
tool_node = ToolNode(tools=tools)
model = llm.bind_tools(tools = tools, strict=True)

def read_human_feedback(state):
    # if state['messages'][-1].tool_calls == []:
    #     logger.info("AI: "+ state['messages'][-1].content)
    #     user_msg = input("Reply: ")
    print("..........",state['messages'][-1].content)
    print("..........",state['messages'][0].content)
    
    history = {"human":f"{state['messages'][0].content}", "ai":f"{state['messages'][-1].content}"}
    print()
    print()
    print(history)
    print()
    print()
    return state
    #     pass

def call_model(state: MessagesState):
    # history = {"human":state["messages"][1], "AI":"This is ai response"}
    print("this is state>>>>>",state)
    messages = [SystemMessage(content=f"You are helpful assistant.\nAs reference, today is {datetime.now().strftime('%Y-%m-%d %H:%M, %A')}.\nKeep a friendly, professional tone.\nAvoid verbosity.\nConsiderations:\n- Don´t assume parameters in call functions that it didnt say.\n- MUST NOT force users how to write. Let them write in the way they want.\n- The conversation should be very natural like a secretary talking with a client.\n- Call only ONE tool at a time.")] + state['messages']
    # messages = [SystemMessage(content="You are a helpful assistant. As reference, today is {datetime.now().strftime('%Y-%m-%d %H:%M, %A')}. Always use tools to answer the queries")]
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