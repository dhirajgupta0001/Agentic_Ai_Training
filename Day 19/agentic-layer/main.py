from fastapi import FastAPI
from agent import call_agent
app=FastAPI()

@app.get("/chat")
async def chat(message:str):
    return await call_agent(message)
