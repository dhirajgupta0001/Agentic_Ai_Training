from langchain.agents import create_agent
from tools import multiply
from middleware import (before_agent_started,
                        after_agent_finished,
                        before_model_started,
                        after_model_finished)

from model import model
Agent=create_agent(
    model=model,
    tools=[multiply],
    middleware=[before_agent_started,
                after_agent_finished,
                before_model_started,
                after_model_finished],
    system_prompt=""" You are a helpful assistant.
    Whenever possible use the available tools."""
)
