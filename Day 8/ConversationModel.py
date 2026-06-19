from langchain_ollama import ChatOllama
from langchain_core.messages import (
    SystemMessage,
    HumanMessage,
    AIMessage
)
model = ChatOllama(
    model="llama3.1",
    temperature=0.7
)

conversation = [
    SystemMessage(content="You are a French translator."),
    HumanMessage(content="Translate: I love programming."),
    AIMessage(content="J'adore la programmation."),
    HumanMessage(content="Translate: I love building applications.")
]

response = model.invoke(conversation)

print(response.content)
