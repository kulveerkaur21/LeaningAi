from dotenv import load_dotenv
load_dotenv()

from typing_extensions import TypedDict, Annotated
from langgraph.graph.message import add_messages
from langgraph.graph import StateGraph, START, END

from pymongo import MongoClient
from langgraph.checkpoint.mongodb import MongoDBSaver

from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-3.5-turbo")

class State(TypedDict):
    messages: Annotated[list, add_messages]

def chatbot(state: State):
    response = llm.invoke(state["messages"])
    return {"messages": [response]}

graph = StateGraph(State)
graph.add_node("chatbot", chatbot)
graph.add_edge(START, "chatbot")
graph.add_edge("chatbot", END)

def compile_graph_with_checkpointer():
    client = MongoClient("mongodb://admin:admin@localhost:27017")
    checkpointer = MongoDBSaver(client)
    return graph.compile(checkpointer=checkpointer)

graph_with_checkpointer = compile_graph_with_checkpointer()

config = {"configurable": {"thread_id": "Kulveer"}}

for chunk in graph_with_checkpointer.stream(
    State({"messages": ["what is my name"]}),
    config,
    stream_mode="values"
    ):
    chunk["messages"][-1].pretty_print()

