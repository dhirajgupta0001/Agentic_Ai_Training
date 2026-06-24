import streamlit as st
from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent

# Model
model = ChatOpenAI(
    api_key="hf_token",
    base_url="https://router.huggingface.co/v1",
    model="meta-llama/Llama-3.1-8B-Instruct:novita",
    temperature=0.7,
)

# Agent
agent = create_react_agent(
    model=model,
    tools=[],
    prompt="""
    You are a senior Python mentor.
    Always explain like a teacher.
    """
)

st.title("Python Mentor Chat")

user_input = st.chat_input("Ask a Python question...")

if user_input:
    with st.chat_message("user"):
        st.write(user_input)

    with st.spinner("Thinking..."):
        response = agent.invoke(
            {
                "messages": [
                    {
                        "role": "user",
                        "content": user_input
                    }
                ]
            }
        )

        answer = response["messages"][-1].content

    with st.chat_message("assistant"):
        st.write(answer)
