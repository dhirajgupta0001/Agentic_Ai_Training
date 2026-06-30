from langchain.agents.middleware import before_agent,after_agent,after_model,before_model

@before_agent
def before_agent_started():
    print("agent started lets kills all the other tasks!!!")

@after_agent
def after_agent_finished():
    print("agent finished")

@before_model
def before_model_started():
    print("model started the tasks lets wait for agent to start and finish!!!")

@after_model
def after_model_finished():
    print("Tool work completed lets wait for agent to complete!!!")
