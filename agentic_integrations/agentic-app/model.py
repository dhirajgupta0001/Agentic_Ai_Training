from dotenv import load_dotenv
load_dotenv()
import os
from langchain_openai import ChatOpenAI
#from langchain.tools import tool
from langchain.agents import create_agent
print(os.getenv("HF_TOKEN"))
model = ChatOpenAI(
      api_key = os.getenv("HF_TOKEN"),
      base_url="https://router.huggingface.co/v1",
      model="meta-llama/Llama-3.1-8B-Instruct:novita",
      temperature=0.7,
  )

agent = create_agent(
    model=model,
    tools=[],
    system_prompt="""
    You are a senior Python mentor.
    Always explain like a teacher.
    """
)
# result = agent.invoke(
#     {
#         "messages": [
#             {
#                 "role": "user",
#                 "content": "Search LangChain"
#             }
#         ]
#     }
# )
# print(result)
