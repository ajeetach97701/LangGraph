from Libs.libs import *

api_key = os.getenv('OPENAI_API_KEY')

def get_llm(model:str='gpt-3.5-turbo'):
    llm=ChatOpenAI(api_key=api_key,model=model,stream_usage=True)
    return llm
        
def get_embeddings():
    embeddings=OpenAIEmbeddings(api_key=api_key)
    return embeddings        