from Libs.libs import *




from nodes import *
# Assistant
# Agent
# RAG_info
# book_me
# handle_greetings


def generate_response(self):
    
    def create_graph(self):
        builder = StateGraph(MessagesState)
        builder.add_node("agent", Agent)
        builder.add_node("assistant", Assistant)
        builder.add_node("rag", RAG_info)
        builder.add_node("book_me", book_me)
        builder.add_node("handle_greetings", handle_greetings)




        builder.add_edge(START, "agent")





        builder.add_edge("rag", END)
        builder.add_edge("book_me", END)



        builder.add_conditional_edges(
            "agent",
        decide_agent,
        )
        builder.add_conditional_edges(
            "assistant",
        decide_assistant
        )

        graph = builder.compile()
        return graph
    graph = create_graph(self)
    if not graph:
        return NotImplementedError("Graph Not Initialized")
    state = MessagesState()
    state['messages'] = self.query
    return graph.invoke(state)


            

        # View
        # display(Image(graph.get_graph().draw_mermaid_png()))