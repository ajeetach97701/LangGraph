from Libs.libs import *


from pydantic import BaseModel
from typing import Literal

members = ["Mercedes", "Lamborghini"]

options = ["FINISH"] + members

class routeResponse(BaseModel):
    next: Literal["Mercedes","Lamborghini","FINISH"]
    
class routeResponse(BaseModel):
    next:Literal['Mercedes', "Lamborghini", 'Coder']

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """You are a supervisor tasked with managing a conversation between the following workers:  {members}. Given the following user request,respond with the worker to act next. Each worker will perform atask and respond with their results and status. When finished,respond with FINISH"""
        ),
        ("placeholder", "{agent_scratchpad}"),
        ("placeholder", "{chat_history}"),
        ("human", "{messages}")
    ]
).partial(options  = str(options), members = ", ".join(members))


def supervisor_agent(state):
    supervisor_chain = (
        prompt| llm.with_structured_output(routeResponse)
    )
    return supervisor_chain.invoke(state)