from Libs.libs import *
from models.vars import DELETE_HISTORY_QUERYS, is_query_exclude

app = FastAPI()
# from graph import graphfrom graph import graph
from Agent.generate_response import GenerateResponse
@app.get('/test')
def test_app():
    return {"message": "this application is up and running"}



REDIS_SERVER = os.getenv('REDIS_SERVER') or 'localhost'


@app.get('/response')
def get_response(query: str, senderId: str, meta_data: Optional[str], latitude: Optional[str] = None, longitude: Optional[str] = None):
    # To clear redis History
    
    if query in DELETE_HISTORY_QUERYS or query == 'menu': 
        history_reddis = RedisChatMessageHistory(
            senderId, url=f"redis://{REDIS_SERVER}")
        history_reddis.clear()
        deleteData(senderId)
    
    if query in DELETE_HISTORY_QUERYS or query == 'menu': 
        deleteData(senderId)
        
    # calling the agent
    is_exist_response = is_query_exclude(query)
    if is_exist_response:
        print()
        print()
        print("The query is:",query)
        print(is_exist_response)
        # print(is_exist_response['title'])
        data:str= ""
        if 'data' in is_exist_response:
            data = is_exist_response['title'] + data
            for item in is_exist_response['data']:
                # print(item['title'])
                data = data+ " " + item['title'] +","
        else:
            data = is_exist_response['title']
        
        print("Data to store in redis is:",data)
        print()
        print()
        return {"custom": is_exist_response}
    
    print(query)
        

    inputs = {"messages":[HumanMessage(content=query)], "senderId":senderId}
    
    data = {"query":query, "senderId":senderId}
    generate_response_instance = GenerateResponse(**data)
    response = generate_response_instance.generate()    
    print("from server",response)
    return response

        


if __name__ == "__main__":
    uvicorn.run(app=app, host="192.168.1.96", port=8000)
