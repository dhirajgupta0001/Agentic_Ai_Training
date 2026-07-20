from langchain.chat_models import init_chat_model

model=init_chat_model("gpt-oss:20b-cloud",
    model_provider="openai",
    api_key="3ebcce2818504f32874cf67012cc6317.C-9s6bKki9tCCDpbzgfWRGNO",
    base_url="https://ollama.com/v1"
)
