
from typing_extensions import TypedDict,Annotated
from langgraph.graph.message import add_messages
from langgraph.graph import StateGraph,START,END
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model_name="gpt-3.5-turbo")

class State(TypedDict):
    messages: Annotated[list,add_messages]

def chatbot(state : State):
    response = llm.invoke(state.get("messages"))
    return { "messages" : [response]}

def simple(state:State):
    print("\n\nInside simplenode",state)
    return {"messages": ["simple message appended"]}

graph = StateGraph(State)
graph.add_node("chatbot",chatbot)
graph.add_node("simplenode",simple)
graph.add_edge(START, "chatbot")
graph.add_edge("chatbot", "simplenode")
graph.add_edge("simplenode", END)

graph_builder = graph.compile()
updatedState = graph_builder.invoke({"messages": "My name is kulveer kaur"})
print("\n\nupdatedstate",updatedState)