from fastapi import FastAPI
from agent import Agent
app=FastAPI()

@app.get("/chat")
def chat(message):
   return Agent.invoke(
            {
                "messages": [
                    {
                        "role": "user",
                        "content": message
                    }
                ]
            }
        )['messages'][-1].content

