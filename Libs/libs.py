import os
import re
import json
import redis
import pprint
import uvicorn
import operator
import requests
import functools
from pydantic import BaseModel, Field

import nest_asyncio
from mdprint import mdprint
import email.message, smtplib
from datetime import datetime
from dotenv import load_dotenv, find_dotenv
from typing import Optional
from langgraph.prebuilt import create_react_agent

from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import END, StateGraph, MessagesState, START
from langchain_core.messages import BaseMessage
from langchain_openai import ChatOpenAI
from typing import Literal
from langgraph.prebuilt import ToolNode
from typing import TypedDict, Annotated, List, Literal,Sequence 
from langchain_core.messages import HumanMessage, SystemMessage, AnyMessage
import datetime
from langchain_core.tools import tool
from typing import Literal
import pandas as pd
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder


from fastapi import FastAPI
from langchain.schema import Document
from langchain_community.document_loaders.csv_loader import CSVLoader
from langchain_text_splitters import RecursiveJsonSplitter
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.tools import Tool,StructuredTool
from langchain.schema.runnable import RunnableMap

from langchain_community.document_loaders import TextLoader

import functools
import operator
from typing import Sequence, Annotated
from typing_extensions import TypedDict
from Redis.utilis import RedisSaver
# from Agent.supervisor_agent import agent_node, supervisor_agent

from langchain_core.messages import BaseMessage



                # from Agent.agent_take2 import *
from Libs.libs import *
# from graph import  graph
from IPython.display import Image, display
from langgraph.graph import END, StateGraph, START
from langgraph.prebuilt import create_react_agent

from langchain_community.callbacks.manager import get_openai_callback


from langchain.memory import ConversationBufferMemory
from langchain.memory import ConversationSummaryMemory
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai.embeddings import OpenAIEmbeddings
from langchain_core.output_parsers import StrOutputParser
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.vectorstores.chroma import Chroma

from langchain_milvus import Milvus
from langchain_core.messages import HumanMessage, AIMessage

from langchain_core.output_parsers.json import JsonOutputParser
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.agents import create_tool_calling_agent, AgentExecutor
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_community.chat_message_histories import RedisChatMessageHistory

from models.model import get_llm, get_embeddings
from models.redis import getData,setData,deleteData,flushAll
llm = get_llm('gpt-4o-mini')


host = os.getenv("HOST")
port = os.getenv("PORT")

REDIS_SERVER=os.getenv('REDIS_SERVER')  or 'localhost'
llm = get_llm('gpt-4o-mini')
embeddings = get_embeddings()

string_parser= StrOutputParser()
json_parser = JsonOutputParser()







from math import radians, sin, cos, sqrt, atan2
