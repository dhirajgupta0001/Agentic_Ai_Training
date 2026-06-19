from langchain_ollama import ChatOllama
model = ChatOllama(
    model="llama3.1",
    temperature=0.7
  )
for chunk in model.stream(
    "Explain quantum computing simply."
):
    print(chunk.content, end="", flush=True)
