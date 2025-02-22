
from Libs.libs import *
def decide_agent(state:GreetingResponse)-> Literal['handle_greetings', "assistant"]:
    check = state["messages"][-1].content
    print()
    print()
    print(check)
    print()
    print()
    if check == 'handle_greetings':
        print('handle_greetings')
        return "handle_greetings"
    else: 
        return "assistant"

def decide_assistant(state) -> Literal['rag', "book_me"]:
    
    check = state["messages"][-1].content
    print()
    print()
    print(state)
    print()
    print()
    if check == 'rag':
        return "rag"
    else: 
        return "book_me"
def decide_assistant_end(state) -> Literal['end']:
    
    check = state["messages"][-1]
    if check == 'rag':
        return "rag"
    else: 
        return "book_me"