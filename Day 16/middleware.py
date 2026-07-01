from langchain.agents.middleware import (
     before_agent,
     after_agent,
     before_model,
     after_model
)

@before_agent
def before_agent_started(self,state):
    print("Agent started!")

@after_agent
def after_agent_finished(self,state):
    print("Agent finished!")

@before_model
def before_model_started(self,state):
    print("Model started!")

@after_model
def after_model_finished(self,state):
    print("Model finished!")
