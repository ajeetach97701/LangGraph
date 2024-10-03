from Libs.libs import *

members = ["Appointments", "Rag"]
system_prompt = (
    "You are a supervisor tasked with managing a conversation between the"
    " following workers:  {members}. Given the following user request,"
    " respond with the worker to act next. Analyze the user query well and then choose members."
    "You do not need to go to all the members for a query When finished,"
    " respond with FINISH. Only invoke one worker at once ."
)
# Our team supervisor is an LLM node. It just picks the next agent to process
# and decides when the work is completed
options = ["FINISH"] + members


class routeResponse(BaseModel):
    next: Literal[*options]


prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        MessagesPlaceholder(variable_name="messages"),
        (
            "system",
            "Given the conversation above, who should act next?"
            " Or should we FINISH? Select one of: {options}",
        ),
    ]
).partial(options=str(options), members=", ".join(members))




def agent_node(state, agent, name):
    result = agent.invoke(state)

    return {
        "messages": [HumanMessage(content=result["output"], name=name)],
        # "messages": [HumanMessage(content=result["messages"][-1].content, name=name)]
    }

def supervisor_agent_make(state):
    supervisor_chain = prompt | llm.with_structured_output(routeResponse)
    
    rsult = supervisor_chain.invoke(state)
    
    return supervisor_chain.invoke(state)