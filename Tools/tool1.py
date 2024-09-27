from mdprint import mdprint

from Libs.libs import *
from Tools.Schema import QueryInput



def Lamborghini(query: str):
    template = """
    You are a tool that answer queries related to Lamborghini vehicle. 
    If the query is other than Lamborghini, say i do not know.
    You are given a human query: {query}

        provide response in 3 sentences in under 30 words and  concise, precise.


                    """
    prompt_temp = ChatPromptTemplate.from_template(template=template
                                                   )

    chain = RunnableMap({
        "query": lambda x: x['query'],
        "cars_context": lambda x: x['cars_context']

    }) | prompt_temp | llm | string_parser
    

    response = chain.invoke({"query": query})
    print(response)
    return response



vehicle_lambo_Tool = StructuredTool.from_function(
        name='vehicleLamboTool',
        func=Lamborghini,
        description="A tool that responds to query related to only Lamborghini.",
        args_schema=QueryInput,
        return_direct=True
    )