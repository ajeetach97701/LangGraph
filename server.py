

import importlib
from models.redis_new import *

from Libs.libs import *
from Schema.databaseState import vector_databases
from src.generate import *

app = FastAPI()
REDIS_SERVER = os.getenv('REDIS_SERVER') or 'localhost'



@app.get('/test')
def test_app():
    return {"message": "this application is up and running"}


@app.get("/", response_class=HTMLResponse)
async def home():
   with open("template.html", "r") as file:
    content = file.read()
   return HTMLResponse(content=content)







@app.get('/response')
# def get_response(query: str, senderId: str):
def get_response(query: str, senderId: str):

    sender = senderId
    global vector_databases
    tool_call_info = {}

    print("---------------Hit in server---------------")
    vector_databases.setdefault('llm', ChatOpenAI(api_key=os.getenv('OPENAI_API_KEY'), model='gpt-4o-mini', stream_usage=True))
    vector_databases.setdefault('embeddings', OpenAIEmbeddings( api_key=os.getenv('OPENAI_API_KEY')))
    sender = senderId
    
    data = {
        "query": query, 
        "senderId": senderId,
        "llm": vector_databases["llm"], 
        "embeddings": vector_databases['embeddings'], 

        }
    history_reddis = RedisChatMessageHistory(senderId,key_prefix="", url=f"redis://{REDIS_SERVER}")

    if query in DELETE_HISTORY_QUERYS:
        history_reddis.clear()
        data['query'] = "Hi"
        generate_response_instance = GenerateResponse(**data)
        response, tool_call_info = generate_response_instance.generate()
        deleteData(senderId)


    
    generate_response_instance = GenerateResponse(**data)
    response = generate_response_instance.generate()


    


    return {"result": response['messages'][-1].content, "duration": "duration.total_seconds()"}




if __name__ == "__main__":
    uvicorn.run(app=app, host="192.168.1.83", port=8000)