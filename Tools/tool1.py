from mdprint import mdprint

from Libs.libs import *
from Tools.Schema import QueryInput



def color2(query: str, organization_name: str):
    template = """
    You are a tool that answer queries related to Lamborghini vehicle. 
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
        func=color2,
        description="A tool that responds to query related to only Lamborghini vehicle.",
        args_schema=QueryInput,
        return_direct=True
    )