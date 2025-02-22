from Libs.libs import *

from Schema.databaseState import vector_databases

from models.db import *

@calculate_time
def RAG_info(state: MessagesState):
    global vector_databases
    print("====RAG TOOL====", state['messages'][-1].content)

    prompt = """
        Given the query and the context, answer the user query from the context. The answer is present in the contex.t Answer from the context.
        \n----------
        query: {query}
        \n----------\n\n
        context: "Ajeet is a Juniro ML Engineer."
        \n----------\n\n
        
    """
    print(state["messages"])
    query = state['messages']
                        
    prompt = ChatPromptTemplate.from_template(prompt)
    context = "Ajeet is a Juniro ML Engineer."
    # collection_name = os.getenv('AjeetRAG')


    # vector_store = vector_databases.get(collection_name)
    # if not vector_store:
    #     vector_store = VectorStore(
    #         collection_name=collection_name, store_type=vector_store, embeddings=embeddings
    #     ).get_vector_store()
    #     vector_databases[collection_name] = vector_store
    # else:
    #     print("Else collection name")

    # context = vector_store.similarity_search(query, k=10)

    chain = RunnableMap({
        'query': lambda x: x['query'],
        "context": lambda x: context
    }) | prompt | llm | string_parser
    res = chain.invoke({"query": query})
    return {"messages":AIMessage(content=res)}
