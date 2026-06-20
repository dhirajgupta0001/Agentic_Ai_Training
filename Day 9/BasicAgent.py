from langchain_openai import ChatOpenAI
from langchain.agents import create_agent

model = ChatOpenAI(
    api_key="hf_token",
    base_url="https://router.huggingface.co/v1",
    model="meta-llama/Llama-3.1-8B-Instruct:novita",
    temperature=0.7,
)

agent = create_agent(
    model=model,
    tools=[]
)

response = agent.invoke(
    {
        "messages": [
            {
                "role": "user",
                "content": "Explain AI simply"
            }
        ]
    }
)

print(response)
