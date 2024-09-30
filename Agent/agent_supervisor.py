from Libs.libs import *
from Tools.Schema import *
from Tools.tool1 import vehicle_lambo_Tool
from Tools.tool2 import vehicleTool


from pydantic import BaseModel
from typing import Literal
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

members = ["Mercedes", "Lamborghini"]

system_prompt = (
    """You are a supervisor tasked with managing a conversation between the following workers:  {members}. Given the following user request,respond with the worker to act next. Each worker will perform atask and respond with their results and status. When finished,respond with FINISH."""
)
# Our team supervisor is an LLM node. It just picks the next agent to process and decides when the work is completed
options = ["FINISH"] + members


# class routeResponse(BaseModel):
#     next: Literal[*options]
    

class routeResponse(BaseModel):
    next: Literal["Mercedes","Lamborghini","FINISH"]

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        MessagesPlaceholder(variable_name="messages"),
        (
            "system",
            """Given the conversation above, who should act next? Or should we FINISH? Select one of: {options}"""
        ),
    ]
).partial(options=str(options), members=", ".join(members))


def supervisor_agent(state):
    supervisor_chain = (
        prompt
        | llm.with_structured_output(routeResponse)
    )
    print("The state is ",state)

    print("The message is ",state)
    result =  supervisor_chain.invoke(state)
    print("The result is", result.next)
    if hasattr(result, 'next'):
            return {
                "messages": state["messages"],
                "next": result.next
            }
    else:
        print("Response does not have 'next'. Returning default state.")
        return {
            "messages": state["messages"],
            "next": "FINISH"
        }
    return supervisor_chain.invoke(message)