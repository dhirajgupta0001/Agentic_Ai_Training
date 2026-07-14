import time
import streamlit as st

from rag import ask

st.set_page_config(
    page_title="Organic Chemistry RAG",
    page_icon="🧪",
)

st.title("🧪 Organic Chemistry Assistant")

if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "Hi! Ask me anything from the NCERT Class 12 Organic Chemistry textbook."
        }
    ]

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if prompt := st.chat_input("Ask your chemistry question..."):

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):

        placeholder = st.empty()

        answer, pages = ask(prompt)

        response = ""

        for word in answer.split():
            response += word + " "
            time.sleep(0.02)
            placeholder.markdown(response + "▌")

        response += f"\n\n📖 **Source Pages:** {', '.join(map(str, pages))}"

        placeholder.markdown(response)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response
        }
    )
