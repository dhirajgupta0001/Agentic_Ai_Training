# from fastapi import FastAPI
# from model import agent
# app=FastAPI()
# @app.get('/chat')

# def read():
#     result = agent.invoke(
#     {
#         "messages": [
#             {
#                 "role": "user",
#                 "content": "Search LangChain"
#             }
#         ]
#     }
#)
# from fastapi import FastAPI
# from pydantic import BaseModel
# from model import agent

# app = FastAPI()

# class ChatRequest(BaseModel):
#     message: str

# @app.post("/chat")
# def chat(request: ChatRequest):
#     result = agent.invoke(
#         {
#             "messages": [
#                 {
#                     "role": "user",
#                     "content": request.message
#                 }
#             ]
#         }
#     )

#     return result
# @app.post("/chat")
# def chat(request: ChatRequest):
#     result = agent.invoke(
#         {
#             "messages": [
#                 {
#                     "role": "user",
#                     "content": request.message
#                 }
#             ]
#         }
#     )

#     return {
#         "response": result["messages"][-1].content
#     }

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from model import agent

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    message: str

@app.get("/")
def root():
    return {"message": "Running Fine Dhiraj"}

@app.post("/chat")
def chat(request: ChatRequest):

    result = agent.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": request.message,
                }
            ]
        }
    )

    return {
        "response": result["messages"][-1].content
    }
