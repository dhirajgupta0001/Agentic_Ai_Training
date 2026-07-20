# from langgraph_supervisor import create_supervisor

# from agents.calculator_agent import call_agent
# from agents.weather_agent import call_agent2
# from model import model


# async def build_supervisor():

#     calculator_agent = await call_agent()
#     weather_agent = await call_agent2()

#     workflow = create_supervisor(
#         agents=[
#             calculator_agent,
#             weather_agent,
#         ],
#         model=model,
#         prompt="""You are a supervisor.

# Delegate all math questions to calculator_agent.

# Delegate all weather questions to weather_agent.

# Never answer directly.
# Always delegate to the appropriate agent.
# """
#     )

#     return workflow.compile()

from langgraph_supervisor import create_supervisor

from model import model
from agents.calculator_agent import build_calculator_agent
from agents.weather_agent import build_weather_agent
async def build_graph():
    calculator_agent = await build_calculator_agent()
    weather_agent = await build_weather_agent()
    workflow = create_supervisor(
    agents=[calculator_agent, weather_agent],
    model=model,
    prompt="""
You are a supervisor.

Your only responsibility is to route the user's request to the correct specialist.

Rules:
- Never answer the user's question yourself.
- Always delegate to exactly one agent.
- Use calculator_agent for any mathematical calculation, arithmetic, algebra, percentages, equations, or numeric operations.
- Use weather_agent for any weather-related question, including temperature, forecast, humidity, rain, wind, or climate.
- After the selected agent responds, return only that agent's final response.
- Do not modify or summarize the agent's response.
"""
)

    return workflow.compile()
