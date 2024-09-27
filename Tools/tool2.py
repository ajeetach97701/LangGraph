from mdprint import mdprint

from Libs.libs import *
from Tools.Schema import QueryInput



def mercedes(query: str):
    template = """
    You are a tool that answer queries related to specs of mercedes vehicle. 
    If the query is other than mercedes, say i do not knoe
    You are given a human query: {query}
         provide response in 3 sentences in under 30 words and  concise, precise.
                    """
    prompt_temp = ChatPromptTemplate.from_template(template=template
                                                   )

    chain = RunnableMap({
        "query": lambda x: x['query'],

    }) | prompt_temp | llm |string_parser

    response = chain.invoke({"query": query})
    print(response)
    return response



vehicleTool = StructuredTool.from_function(
        name='vehicleTool',
        func=mercedes,
        description="A tool that responds to query related to only Mercedes.",
        args_schema=QueryInput,
        return_direct=True
    )