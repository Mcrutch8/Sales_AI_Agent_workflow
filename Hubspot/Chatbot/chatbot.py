from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env

# Get API key from environment
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("OPENAI_API_KEY not found. Please set it in your .env file.")

from typing import Annotated
from typing_extensions import TypedDict

from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages

# Define State with message tracking
class State(TypedDict):
    messages: Annotated[list, add_messages]

# Initialize LangGraph
graph_builder = StateGraph(State)

# Initialize OpenAI LLM
from langchain_openai import ChatOpenAI

# Here we are adding a chatbot node in which a node represents a unit of work. This is really just 
# a python function

llm = ChatOpenAI(model="gpt-4o-mini")  

def chatbot(state: State):
    return {"messages": [llm.invoke(state["messages"])]}

# The first argument is the unique node name
# The second argument is the function or object that will be called whenever
# the node is used.
graph_builder.add_node("chatbot", chatbot)

# add an entry point. This tells our graph where to start its work each time we run it.
graph_builder.add_edge(START, "chatbot")

# set a finish point. This instructs the graph "any time this node is run, you can exit."
graph_builder.add_edge("chatbot", END)

# Finally, we'll want to be able to run our graph. To do so, call "compile()" on the graph builder. 
# This creates a "CompiledGraph" we can use invoke on our state.
graph = graph_builder.compile()

def stream_graph_updates(user_input: str):
    for event in graph.stream({"messages": [{"role": "user", "content": user_input}]}):
        for value in event.values():
            print("Assistant:", value["messages"][-1].content)


while True:
    try:
        user_input = input("User: ")
        if user_input.lower() in ["quit", "exit", "q"]:
            print("Goodbye!")
            break

        stream_graph_updates(user_input)
    except:
        # fallback if input() is not available
        user_input = "What do you know about LangGraph?"
        print("User: " + user_input)
        stream_graph_updates(user_input)
        break

