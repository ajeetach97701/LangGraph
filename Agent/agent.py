from Libs.libs import *
# from models.db import VectorStore
from Tools.Schema import *
from Tools.tool1 import vehicle_lambo_Tool
from Tools.tool2 import vehicleTool

#used to track the cost of API calls when working with OpenAI models.
from langchain.callbacks import get_openai_callback

REDIS_SERVER = os.getenv('REDIS_SERVER') or 'localhost'

def create_custom_agent(prompt, tools:list):
    print("entered here in the agent")
# def generate_response(query):
    prompt_agent = ChatPromptTemplate.from_messages(
        [
            (
                "system",prompt
            
            ),
            ("placeholder", "{chat_history}"),
            ("human", "{messages}"),
            ("placeholder", "{agent_scratchpad}"),
        ],
    )

    agent = create_tool_calling_agent(llm, tools, prompt_agent)

    agent_executor = AgentExecutor(tools=tools,
                                   return_intermediate_steps=True,
                                   handle_parsing_errors=True,
                                   max_iterations=5,
                                   early_stopping_method='generate',
                                   agent=agent,
                                   verbose=True
                                   )
    return agent_executor

def agent_node(state, agent, name):
    result = agent.invoke(state)
    print(result)
    return {
        "messages": state["messages"] + [HumanMessage(content=result['output'], name=name)],
        "next": "supervisor"  # Assuming you want to go to supervisor next
    }
    # return {"message":[HumanMessage(content=result['output'],next = name)]}