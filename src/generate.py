
from Libs.libs import *
from graph.graph import generate_response 
# buffer convo save
user_conversations = {}


class QueryRequest(BaseModel):
    query: str =  Field(description="Query to be passed as an argument. Always use this")
    senderId: str =  Field(description="Sender id to be passed as an argument. Always use this")
   
class GenerateResponse:

    def __init__(self, **requestData: QueryRequest):
        for key, value in requestData.items():
            setattr(self, key, value)

        # self.history=RedisChatMessageHistory(self.sender, url=f"redis://{self.redis_server}",ttl=60*60*8)

    def generate(self):
        response = generate_response(self)
        return response
