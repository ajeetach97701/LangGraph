from Libs.libs import *

from pydantic import BaseModel, Field
from typing import Literal, Union
from langchain_openai import ChatOpenAI
import os
from langchain_core.prompts import ChatPromptTemplate

# Initialize LLM



@calculate_time
def Agent(state:MessagesState) -> Literal['handle_greetings', "assistant"]:
    try:
        print("Inside Agent")
        print(state['messages'][-1])

        print("------------------------")
        # System Prompt
        system_prompt = """
            You are an expert at routing a user question to either 'handle_greetings' or 'assistant'.
            - If the query is salutations: return only handle_greetings
            - For all other queries except greetings, return: assistant.
        """
                            
        prompt = ChatPromptTemplate.from_messages([
            ("system", system_prompt),
            ("human", "{query}"),
        ])

        query = state['messages']

        new_llm = llm.with_structured_output(schema=GreetingResponse)
        chain = prompt | new_llm
        response = chain.invoke({"query": query})

        state['messages'] = response.type
        print("From Agent Node:")
        print(state)
        print("================")
        return state

        
    except Exception as e:
        return str(e)



"""For testing   this file only"""
# state = MessagesState(messages="tell me about ai")

# print(Agent(state))  
