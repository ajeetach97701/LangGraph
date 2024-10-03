import functools
import operator
from typing import Sequence, Annotated
from typing_extensions import TypedDict
from Redis.utilis import RedisSaver
# from Agent.supervisor_agent import agent_node, supervisor_agent

from langchain_core.messages import BaseMessage

from langgraph.graph import END, StateGraph, START
from langgraph.prebuilt import create_react_agent
from Libs.libs import *
from Tools.tools_init_ import GetCustomTools
from Tools.availability_by_doctor import check_availability_by_doctor
from Tools.availability_by_specialization import check_availability_by_specialization
from Tools.booking import book_appointment
from Tools.reschedule import reschedule
from Tools.ragAgent import rag_tool
from Agent.supervisor_agent import supervisor_agent_make, agent_node

# The agent state is the input to each node in the graph
class AgentState(TypedDict):
    # The annotation tells the graph that new messages will always
    # be added to the current states
    messages: Annotated[Sequence[BaseMessage], operator.add]
    # The 'next' field indicates where to route to next
    next: str

def graph(request_data):
    def graph_main():

        def read_human_feedback(state):
            return state
        
        def should_continue(state: MessagesState) -> Literal["tools", "human_feedback"]:
            messages = state['messages']
            last_message = messages[-1]
            if last_message.tool_calls:
                return "tools"
            return "human_feedback"
        
        def should_continue_with_feedback(state: MessagesState) -> Literal["supervisor_agent", "end", "human_feedback"]:
            messages = state['messages']
            last_message = messages[-1]
            if isinstance(last_message, dict):
                if last_message.get("type","") == 'human_feedback':
                    return "agent"
            if (isinstance(last_message, HumanMessage)):
                return "agent"
            if (isinstance(last_message, AIMessage)):
                return "end"
            return "end"
       
        
        toolsInstance = GetCustomTools()
        tools_available = toolsInstance.get_tools()

        
    Appointments_agnet = create_react_agent(llm, tools=tools_available, )
    Appointments_node = functools.partial(agent_node, agent=Appointments_agnet, name="Appointments")

    Rag_agent = create_react_agent(llm, tools=[rag_tool])
    Rag_node = functools.partial(agent_node, agent=Rag_agent, name="Rag")
    workflow = StateGraph(AgentState)
    workflow.add_node("Appointments", Appointments_node)
    workflow.add_node("Rag", Rag_node)
    workflow.add_node("supervisor_agent", supervisor_agent_make)
    workflow.add_node("human_feedback", read_human_feedback)

    # workflow.add_edge("Appointments", "supervisor_agent")
    conditional_map = {'Appointments': 'Appointments', 'Rag': 'Rag', 'FINISH': '__end__'}
    # workflow.add_conditional_edges("supervisor_agent", lambda x: x["next"], conditional_map)

    workflow.add_conditional_edges(
    "supervisor_agent",
    should_continue,
            {
                "human_feedback":"human_feedback",
                "Rag":"Rag",
                "Appointments":"Appointments"}
        )
    workflow.add_conditional_edges(
        "human_feedback",
        should_continue_with_feedback,
        {"supervisor_agent":"supervisor_agent","end":END}
    )

    workflow.add_conditional_edges(
        "Appointments",
        should_continue_with_feedback,
        {"supervisor_agent":"supervisor_agent","end":END}
    )

    workflow.add_conditional_edges(
        "Rag",
        should_continue_with_feedback,
        {
            "supervisor_agent":"supervisor_agent",
            "end":END
            }
    )
            
            
            
    workflow.add_edge(START, "supervisor_agent")
    graph = workflow.compile()



   
   
    for s in graph.stream({"messages": [HumanMessage(content=request_data.query)]},{"recursion_limit": 100}):
        if "__end__" not in s:
            print(s)
            print("----")
        else:
            print(s)

    # with RedisSaver.from_conn_info(host="localhost", port=6379, db=0) as checkpointer:
    #     graph = workflow.compile(checkpointer=checkpointer)
    #     inputs = {"messages": [HumanMessage(content=query)], "senderId": "senderId"}
    #     config = {"configurable": {"thread_id": "senderId"}}

    #     for s in graph.stream({"messages": [HumanMessage(content=query)]},{"recursion_limit": 100}):
    #        if "__end__" not in s:
    #            print(s)
    #            print("----")
                    
                    
                    
                    
    #                 # print({"result": final_response, "token_usage": token_usage})
                
            
        return graph_main()


            








            