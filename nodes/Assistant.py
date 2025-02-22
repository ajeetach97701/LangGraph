from Libs.libs import *

from pydantic import BaseModel, Field
from typing import Literal, Union
from langchain_openai import ChatOpenAI
import os
from langchain_core.prompts import ChatPromptTemplate

# Initialize LLM
class AssistantResponse(BaseModel):
    type: str
    # hire: str = Field(..., description= "The Greeting responses for the given query")
    # rag: str = Field(..., description= "The Greeting responses for the given query")
    
@calculate_time
def Assistant(state:MessagesState) -> AssistantResponse:
    try:
        print("entered inside Assistant node")
        print("------------------------")
        print(state['messages'][-1])
        # System Prompt
        system_prompt = """
            Given the user query, analyze it and return only one word output. The options are:
            - hire:  If the query is related to hiring Ajeet.
            - rag: If the query is related to knowing about Ajeet.
            - END
        """
                            
        prompt = ChatPromptTemplate.from_messages([
            ("system", system_prompt),
            ("human", "{query}"),
        ])

        query = state['messages']

        # Use LangChain LLM with structured output
        new_llm = llm.with_structured_output(schema=AssistantResponse)
        chain = prompt | new_llm
        response = chain.invoke({"query": query})
        print("From Assistant")
        state['messages'] = response.type
        print(state)
        return state
        
    except Exception as e:
        return str(e)



"""For testing   this file only:
insert this piece of code in test.ipynb file and run the cell.
"""

# from nodes.handle_greetings import *
# state = MessagesState(messages="tell me about ai")

# print(handle_greetings(state))  
