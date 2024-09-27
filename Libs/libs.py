from dotenv import load_dotenv, find_dotenv
import os
import json
import requests
import re
import redis
import pprint
import uvicorn
import nest_asyncio
from mdprint import mdprint
import email.message, smtplib



from typing import Optional


from fastapi import FastAPI
from langchain.schema import Document
from langchain_community.document_loaders.csv_loader import CSVLoader
from langchain_text_splitters import RecursiveJsonSplitter
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.tools import Tool,StructuredTool
from langchain.schema.runnable import RunnableMap
from langchain.document_loaders import TextLoader
from pydantic import BaseModel, Field
from langchain.callbacks import get_openai_callback
from langchain.memory import ConversationBufferMemory
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.memory import ConversationSummaryMemory
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai.embeddings import OpenAIEmbeddings
from langchain_core.output_parsers import StrOutputParser
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.vectorstores.chroma import Chroma
from langchain_community.vectorstores.milvus import Milvus
from langchain_core.messages import HumanMessage, AIMessage

from langchain_core.output_parsers.json import JsonOutputParser
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.agents import create_tool_calling_agent, AgentExecutor
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_community.chat_message_histories import RedisChatMessageHistory

    
from models.vars import DELETE_HISTORY_QUERYS
from models.model import get_llm, get_embeddings
from models.model import get_embeddings, get_llm
from models.redis import getData,setData,deleteData,flushAll




REDIS_SERVER=os.getenv('REDIS_SERVER')  or 'localhost'
llm = get_llm('gpt-4o-mini')
embeddings = get_embeddings()

string_parser= StrOutputParser()
json_parser = JsonOutputParser()

import functools
import operator 
from typing import Sequence, Annotated
from typing_extensions import TypedDict
from langchain_core.messages import BaseMessage
from langgraph.graph import END, StateGraph, START
from Libs.libs import *
from langgraph.prebuilt import create_react_agent
from Agent.agent import create_custom_agent, agent_node

from Agent.agent_supervisor import supervisor_agent
from Tools.tool1 import vehicle_lambo_Tool
from Tools.tool2 import vehicleTool







from math import radians, sin, cos, sqrt, atan2
