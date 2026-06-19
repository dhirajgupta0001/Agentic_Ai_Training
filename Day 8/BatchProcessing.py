from langchain_ollama import ChatOllama
model = ChatOllama(
    model="llama3.1",
    temperature=0.7
  )
responses = model.batch([
    "What is Python?",
    "What is AI?",
    "What is LangChain?"
])

for r in responses:
    print(r.content)
