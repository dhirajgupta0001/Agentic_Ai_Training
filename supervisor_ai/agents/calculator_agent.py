from langchain.agents import create_agent
from model import model
from tools.calculator_tool import get_tools

async def build_calculator_agent():
    tools=await get_tools()
    return create_agent(
        model=model,
        tools=tools,
        system_prompt="""
You are a calculator expert.

Always use the calculator tools whenever the user asks
for mathematical calculations.

Never calculate yourself if a tool is available.
""",
name="calculator_agent"
)
    # response=await agent.ainvoke({"messages":
    #                               [{
    #                                 "role":"user",
    #                                 "content":message
    #                                }
    #                               ]})
    # return response["messages"][-1].content
        
