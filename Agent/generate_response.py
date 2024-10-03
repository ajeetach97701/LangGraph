from Libs.libs import *
from graph import graph

from models.Schema import QueryInput


class GenerateResponse:

    def __init__(self, **requestData: QueryInput):
        for key, value in requestData.items():
            setattr(self, key, value)

        # self.history=RedisChatMessageHistory(self.sender, url=f"redis://{self.redis_server}",ttl=60*60*8)

    def generate(self):
        return graph(self)
