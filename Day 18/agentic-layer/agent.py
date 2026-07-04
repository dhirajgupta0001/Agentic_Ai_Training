from langchain.agents import create_agent
from model import model
from tools import get_tools
async def call_agent(message:str):
    tools=await get_tools()
    agent=create_agent(
        model=model,
        tools=tools,
        system_prompt="""You are a helpful assistant.
    Whenever possible use the available tools."""

    )
    response=await agent.ainvoke({"messages":
                                  [{
                                    "role":"user",
                                    "content":message
                                   }
                                  ]})
    return response["messages"][-1].content
