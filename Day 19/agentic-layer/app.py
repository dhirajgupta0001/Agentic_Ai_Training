import streamlit as st
import time
import asyncio
from agent import call_agent


def run_async(coro):
    """Run async code safely inside Streamlit."""
    try:
        loop = asyncio.get_event_loop()

        if loop.is_closed():
            raise RuntimeError

    except RuntimeError:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

    return loop.run_until_complete(coro)


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

    # Assistant response
    with st.chat_message("assistant"):

        message_placeholder = st.empty()
        full_response = ""

        # Run async agent
        assistant_response = run_async(call_agent(message))

        # Typing animation
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
