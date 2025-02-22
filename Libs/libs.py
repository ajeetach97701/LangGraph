from langgraph.graph import MessagesState
import os
from typing import Literal




import re
import json
import pprint
import pprint
import uvicorn
import datetime
import requests
import json ,csv
import nest_asyncio
from enum import Enum
from pathlib import Path
from typing import Optional
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from langchain_community.document_loaders import PyMuPDFLoader

from IPython.display import Image, display
from langgraph.graph import StateGraph, START, END
from langgraph.graph import MessagesState
from langgraph.prebuilt import ToolNode
from langgraph.prebuilt import tools_condition





from redis import Redis

import email.message, smtplib
from langchain_milvus import Milvus

from langchain.schema import Document
from pydantic import BaseModel, Field
# from Schema.prompts import get_prompts
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv, find_dotenv
from langchain.prompts import PromptTemplate
from langchain.tools import Tool,StructuredTool
from langchain.schema.runnable import RunnableMap
from pymilvus import connections,utility,Collection
from langchain.memory import ConversationBufferMemory
from langchain_core.prompts import ChatPromptTemplate
from langchain.memory import ConversationSummaryMemory
from langchain_openai.embeddings import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain_core.output_parsers import StrOutputParser
from langchain_text_splitters import RecursiveJsonSplitter
from langchain_core.messages import HumanMessage, AIMessage
from langchain_community.document_loaders import TextLoader
from langchain_core.output_parsers.json import JsonOutputParser
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders.csv_loader import CSVLoader
from langchain.agents import create_tool_calling_agent, AgentExecutor
from langchain_community.callbacks.manager import get_openai_callback
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_community.chat_message_histories import RedisChatMessageHistory


load_dotenv(find_dotenv())


class Config:
    GENERAL_HYUNDAI = os.getenv('GENERAL_HYUNDAI')
    VEHICLE_HYUNDAI = os.getenv('VEHICLE_HYUNDAI')
    VEHICLE_FEATURES_HYUNDAI = os.getenv('VEHICLE_FEATURES_HYUNDAI')
    CHARGING_HYUNDAI = os.getenv('CHARGING_HYUNDAI')
    SERVICE_HYUNDAI = os.getenv('SERVICE_HYUNDAI')

from Schema.states import *


string_parser= StrOutputParser()
json_parser = JsonOutputParser()


from customDecorator.decorator import calculate_time



REDIS_SERVER=os.getenv('REDIS_SERVER')
# host = "192.168.1.100"
# port = "19530"

host = os.getenv("HOST")
port = os.getenv("PORT")


URI = f"http://{host}:{port}"
# connection_args  ={
#     "uri":URI
# }
llm = ChatOpenAI(api_key=os.getenv("OPENAI_API_KEY"), model="gpt-4o-mini")
from langchain_core.messages import HumanMessage, ToolMessage

connection_args={
    "uri": URI
    # "host": host,
    # "port": port 
                 }


from Schema.states import *