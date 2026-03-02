
from typing import Optional,Literal
from dotenv import load_dotenv
load_dotenv()

from langchain_openai import ChatOpenAI
llm = ChatOpenAI(model="gpt-3.5-turbo")

from typing_extensions import TypedDict,Annotated
from langgraph.graph.message import add_messages
from langgraph.graph import StateGraph,START,END

class state(TypedDict):
    userquery : str
    llm_output : Optional[str]
    is_good : Optional[bool]

def chatbot(state:state):
    response = llm.invoke(state["userquery"])
    state["llm_output"] = response.content
    return state

def evaluate(state:state) -> Literal["chatbat_gemini","end"]:
    if True:
       return "end"
    return "chatbat_gemini"

def chatbat_gemini(state:state):
    response = llm.invoke(state["userquery"])
    state["llm_output"] = response.content
    return state

def end(state:state):
    return state
graph = StateGraph(state)
graph.add_node("chatbot", chatbot)
graph.add_node("evaluate", evaluate)
graph.add_node("chatbat_gemini", chatbat_gemini)
graph.add_node("end", end)

graph.add_edge(START, "chatbot")
graph.add_conditional_edges("chatbot", evaluate)


graph.add_edge("chatbat_gemini", "end")
graph.add_edge("end", END)
graph_builder = graph.compile()
updated_State = graph_builder.invoke(state({"userquery" : "hey what is 2+2?"}))
print("updatedsttae",updated_State)

