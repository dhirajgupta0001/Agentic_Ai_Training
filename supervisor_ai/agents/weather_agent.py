from langchain.agents import create_agent
from model import model
from tools.weather_tool import get_tools

async def build_weather_agent():
    tools=await get_tools()
    return create_agent(
        model=model,
        tools=tools,
        system_prompt="""
You are a weather assistant.

Always use the current_weather tool for every weather-related question.

Do not answer from your own knowledge.

After calling the tool, summarize the returned weather information in a friendly sentence.
""",
name="weather_agent"
)
    # response=await agent.ainvoke({"messages":
    #                               [{
    #                                 "role":"user",
    #                                 "content":message
    #                                }
    #                               ]})
    # return response["messages"][-1].content
                
