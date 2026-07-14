from langchain.chat_models import init_chat_model

# model=init_chat_model(
#   "ollama:llama3.1",
#   temperature=0)

model=init_chat_model("gpt-oss:20b-cloud",
    model_provider="openai",
    api_key="hh",
    base_url="https://ollama.com/v1"
)
