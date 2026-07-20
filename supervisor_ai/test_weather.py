import asyncio
from pprint import pprint

from agents.weather_agent import call_agent2

async def main():
    agent = await call_agent2()

    result = await agent.ainvoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": "What is the weather in Delhi?"
                }
            ]
        }
    )

    pprint(result)

asyncio.run(main())
