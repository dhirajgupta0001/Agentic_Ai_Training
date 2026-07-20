# from fastapi import FastAPI
# from supervisor import build_graph

# app = FastAPI()


# @app.get("/chat")
# async def call_supervisor(question: str):
#     result = await graph.ainvoke(
#         {
#             "messages": [
#                 {
#                     "role": "user",
#                     "content": question,
#                 }
#             ]
#         }
#     )

#     return result["messages"][-1].content
from contextlib import asynccontextmanager

from fastapi import FastAPI

from supervisor import build_graph


@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.graph = await build_graph()
    print("Supervisor graph initialized successfully.")
    yield


app = FastAPI(lifespan=lifespan)


@app.get("/chat")
async def chat(question: str):
    result = await app.state.graph.ainvoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": question,
                }
            ]
        }
    )

    return {
        "response": result["messages"][-1].content
    }
