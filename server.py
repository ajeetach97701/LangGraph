from Libs.libs import *
from models.vars import DELETE_HISTORY_QUERYS, is_query_exclude

app = FastAPI()
from Agent.agent_take2 import graph

@app.get('/test')
def test_app():
    return {"message": "this application is up and running"}



REDIS_SERVER = os.getenv('REDIS_SERVER') or 'localhost'


@app.get('/response')
def get_response(query: str, senderId: str):
    # To clear redis History
    if query in DELETE_HISTORY_QUERYS or query == 'menu': 
        history_reddis = RedisChatMessageHistory(
            senderId, url=f"redis://{REDIS_SERVER}")
        history_reddis.clear()
        deleteData(senderId)
    
    print(query)
        

    inputs = {"messages":[HumanMessage(content=query)], "senderId":senderId}
    
    
    response = graph(query=query, senderId= senderId)
    print("from server",response)
    return response

        


if __name__ == "__main__":
    uvicorn.run(app=app, host="192.168.1.77", port=8000)
