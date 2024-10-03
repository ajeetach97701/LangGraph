
from Libs.libs import *
collection_name: str = os.getenv("RAG_GYM")
from Tools.Schema import RagInput

vector_store=Milvus(embedding_function=embeddings,connection_args={ "host":host, "port":port},collection_name=collection_name)



def create_custom_agent(query:str, prompt:str, tools:list):

    prompt_agent = ChatPromptTemplate.from_messages(
        [
            (
                "system",prompt
            ),
            ("placeholder", "{chat_history}"),
            ("human", "{input}"),
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

 
    output = agent_executor.invoke({"input": query})
    return output


def rag_gym(query: str):
    print("<><><><><><><><><><><> from RAG Tool")

    context = vector_store.similarity_search(query, k=4)

    pprint.pprint(context)
    template = """You are given a context and a human query.
    Do not ever answer using your own knowledge base. 

    Human query is: {query}
    Context is :{context}
    Analyze the human query and context and answer the question related 
    Always ignore the place name mentioned in the query for each and every qeury as the place name does not matter .
    Your response should be precise, concise and not contain any irrelevant information.

    
    """
    prompt = ChatPromptTemplate.from_template(template=template)

    chain = RunnableMap({
        'query': lambda x: x['query'],
        "context": lambda x: vector_store.similarity_search(x['query'], k=6),
    }) | prompt | llm | string_parser

    res = chain.invoke({
        "query": query,
        })

    return res


rag_tool = StructuredTool.from_function(name='bookingTool',
                                                      func=rag_gym,
                                                      description="A tool that is used to answer all the questions related to TATA Punch ev",
                                                      args_schema=RagInput)
