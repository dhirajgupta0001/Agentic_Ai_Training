from langchain_ollama import ChatOllama
llm=ChatOllama(model="llama3.1")
response = llm.invoke("Why do parrots talk?")
print(response.content)
