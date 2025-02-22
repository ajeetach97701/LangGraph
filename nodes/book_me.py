from Libs.libs import *


from models.db import *

def book_me(state: MessagesState):
    print("Inside Book Me")
    query = state['messages'][-1].content
    print(state['messages'][-1])

    return {'messages':"You have booked me sucessfully"}
