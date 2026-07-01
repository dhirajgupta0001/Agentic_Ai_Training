import streamlit as st
import time
from agent import Agent

st.title("Dhiraj's Assistant")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "Let's start chatting! 👇"
        }
    ]

# Display previous messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User input
if message := st.chat_input("What is up?"):

    # Store and display user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": message
        }
    )

    with st.chat_message("user"):
        st.markdown(message)

    # Get assistant response
    with st.chat_message("assistant"):

        message_placeholder = st.empty()
        full_response = ""

        result = Agent.invoke(
            {
                "messages": [
                    {
                        "role": "user",
                        "content": message
                    }
                ]
            }
        )

        assistant_response = result["messages"][-1].content

        for chunk in assistant_response.split():
            full_response += chunk + " "
            time.sleep(0.05)
            message_placeholder.markdown(full_response + "▌")

        message_placeholder.markdown(full_response)

    # Save assistant response
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": full_response
        }
    )
