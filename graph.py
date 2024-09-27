from Libs.libs import *
from langgraph.graph.message import add_messages
from Agent.agent_supervisor import members




mercedes_agent= create_custom_agent(prompt="You answer about mercedes car in 50 words.", tools=[vehicleTool])
lambo_agent = create_custom_agent(prompt="You answer about Lamborghini car in 50 words.", tools=[vehicle_lambo_Tool])


# Agent - 1: Mercedes that has one tool
mercedes_node = functools.partial(agent_node, agent=mercedes_agent, name="Mercedes")
# Agent 2 : Lamborghini that has one tool
lambo_node = functools.partial(agent_node, agent=lambo_agent, name="Lamborghini")

class State(TypedDict):
    messages:Annotated[list, add_messages]# message add garne to keep track of the state
    next:str
    

# class AgentState(TypedDict):
#     messages: Annotated[list, operator.add]
    
workflow = StateGraph(State)
workflow.add_node("Mercedes", mercedes_node)
workflow.add_node("Lamborghini", lambo_node)

workflow.add_node("supervisor", supervisor_agent)


workflow.add_edge(START, "supervisor")

for member in members:
    workflow.add_edge(member, "supervisor")
    
conditional_map = {k:k for k in members} ##  {'Mercedes': 'Mercedes', 'Lamborghini': 'Lamborghini'}
workflow.add_conditional_edges("supervisor", lambda x :x['next'], conditional_map)

conditional_map['FINISH'] = END

graph = workflow.compile()


# user_input = "Tell me about mercedes g wagon and lamborghini urus"
user_input = input()
for s in graph.stream({"messages": [
            HumanMessage(
                content=user_input
            )
        ],
    },):
    if "__end__" not in s:
        print(s)
        print("-----")