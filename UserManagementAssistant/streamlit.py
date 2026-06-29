import time
import streamlit as st

from langchain_core.messages import HumanMessage, AIMessage
from model import agent

st.set_page_config(page_title="User Manager", page_icon="👤")

st.title("👤 User Management Assistant")

# -------------------------------
# Chat History
# -------------------------------
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "Hello! How can I help you today?"
        }
    ]

# Display history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# -------------------------------
# User Input
# -------------------------------
prompt = st.chat_input("Ask something...")

if prompt:

    # Display user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt,
        }
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    # -------------------------------
    # Convert chat history to LangChain messages
    # -------------------------------
    lc_messages = []

    for msg in st.session_state.messages:

        if msg["role"] == "user":
            lc_messages.append(HumanMessage(content=msg["content"]))

        elif msg["role"] == "assistant":
            lc_messages.append(AIMessage(content=msg["content"]))

    # -------------------------------
    # Invoke Agent
    # -------------------------------
    response = agent.invoke(
        {
            "messages": lc_messages
        }
    )

    last_message = response["messages"][-1]
    content = last_message.content

    # -------------------------------
    # Extract text safely
    # -------------------------------
    if isinstance(content, str):
        assistant_response = content

    elif isinstance(content, list):

        text_parts = []

        for block in content:

            if isinstance(block, dict):

                if block.get("type") == "text":
                    text_parts.append(block.get("text", ""))

            else:
                text_parts.append(str(block))

        assistant_response = "\n".join(text_parts)

    else:
        assistant_response = str(content)

    # -------------------------------
    # Display typing effect
    # -------------------------------
    with st.chat_message("assistant"):

        placeholder = st.empty()
        full_response = ""

        for word in assistant_response.split():

            full_response += word + " "

            placeholder.markdown(full_response + "▌")

            time.sleep(0.03)

        placeholder.markdown(full_response)

    # Save assistant message
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": full_response,
        }
    )
