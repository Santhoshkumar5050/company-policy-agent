from langgraph.graph import StateGraph, START, END
from langchain_ollama import ChatOllama
from retrieval import search_policy

llm = ChatOllama(model="llama3")

class State(dict):
    question: str
    plan: list
    context: list
    answer: str

graph = StateGraph(State)

# --- PLAN NODE ---
def plan_node(state):
    response = llm.invoke(
        f"Break the following question into 2–3 sub-questions:\n{state['question']}"
    )
    plan = [line.strip() for line in response.content.split("\n") if line.strip()]
    state["plan"] = plan
    return state

# --- RETRIEVE NODE ---
def retrieve_node(state):
    ctx = []
    for subq in state["plan"]:
        results = search_policy(subq)
        ctx.extend(results)
    state["context"] = ctx
    return state

# --- ANSWER NODE ---
def answer_node(state):
    response = llm.invoke(
        f"""
Using this company policy context:
{state['context']}

Answer this question clearly and accurately:
{state['question']}
"""
    )
    state["answer"] = response.content
    return state

# Add nodes
graph.add_node("plan", plan_node)
graph.add_node("retrieve", retrieve_node)
graph.add_node("answer", answer_node)

# Add edges
graph.add_edge("plan", "retrieve")
graph.add_edge("retrieve", "answer")
graph.add_edge("answer", END)

# ⭐ FIX: Define entrypoint using START
graph.add_edge(START, "plan")

# Compile graph (no entrypoint needed)
agent = graph.compile()
