from Libs.libs import *

from pydantic import BaseModel, Field
from typing import Literal, Union
from langchain_openai import ChatOpenAI
import os
from langchain_core.prompts import ChatPromptTemplate





def handle_greetings(state:MessagesState):
    try:
        print("entered inside handle_greetings node")
        # System Prompt
        system_prompt = """
            You are an expert at handling greeting queries. Response politely and nicely in a human-like way to the human query.
        """
                            
        prompt = ChatPromptTemplate.from_messages([
            ("system", system_prompt),
            ("human", "{query}"),
        ])

        query = state['messages'][-1].content

        # Use LangChain LLM with structured output
        chain = prompt | llm
        response = chain.invoke({"query": query})
        return {"messages":response}

        
    except Exception as e:
        return str(e)



"""For testing   this file only:
insert this piece of code in test.ipynb file and run the cell.
"""

# from nodes.handle_greetings import *
# state = MessagesState(messages="tell me about ai")

# print(handle_greetings(state))  
