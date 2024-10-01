# from Libs.libs import *
# from langgraph.graph.message import add_messages
# from Agent.agent_supervisor import members, options



# from typing import List
# # mercedes_agent= create_custom_agent(prompt="You are provided tools. Answer using the tools", tools=[vehicleTool])
# # lambo_agent = create_custom_agent(prompt="You are provided tools. Answer using the tools", tools=[vehicle_lambo_Tool])


# # Agent - 1: Mercedes that has one tool
# mercedes_node = functools.partial(agent_node, agent=mercedes_agent, name="Mercedes")
# # Agent 2 : Lamborghini that has one tool
# lambo_node = functools.partial(agent_node, agent=lambo_agent, name="Lamborghini")

# class State(TypedDict):
#     messages: Annotated[List[BaseMessage], operator.add]
# # message add garne to keep track of the state
#     next:str
    

# # class AgentState(TypedDict):
# #     messages: Annotated[list, operator.add]
    
# workflow = StateGraph(State)
# workflow.add_node("Mercedes", mercedes_node)
# workflow.add_node("Lamborghini", lambo_node)
# workflow.add_node("supervisor", supervisor_agent)



# for member in members:
#     workflow.add_edge(member, "supervisor")
    
# conditional_map = {k:k for k in members} ##  {'Mercedes': 'Mercedes', 'Lamborghini': 'Lamborghini'}
# conditional_map['FINISH'] = END

# workflow.add_conditional_edges("supervisor", lambda x :x['next'], conditional_map)
# workflow.add_edge(START, "supervisor")

# graph = workflow.compile()

# # def enter_chain(message:str):
# #     results = {
# #         "messages":[HumanMessage(content=message)],
# #     }
# #     return results

# # research_chain = enter_chain| graph