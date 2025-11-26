import streamlit as st
from agent import agent

st.title("🏢 Smart Company Policy Agent (Agentic RAG)")
st.write("Ask anything about company policies.")

question = st.text_input("Enter your question:")

if question:
    st.write("🤖 Thinking...")
    result = agent.invoke({"question": question})
    st.subheader("Answer:")
    st.write(result["answer"])
