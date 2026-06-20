# LangChain Agents with Hugging Face Router + Llama 3.1

A beginner-friendly guide to building LangChain Agents using Hugging Face Router and Llama 3.1.

---

# Overview

This project uses:

* LangChain
* LangGraph
* Hugging Face Router
* Meta Llama 3.1 8B Instruct
* Agent Framework
* Tools
* Memory
* Structured Output
* Middleware

Model Configuration:

```python
from langchain_openai import ChatOpenAI

model = ChatOpenAI(
    api_key="YOUR_HF_TOKEN",
    base_url="https://router.huggingface.co/v1",
    model="meta-llama/Llama-3.1-8B-Instruct:novita",
    temperature=0.7,
)
```

---

# Installation

Install dependencies:

```bash
uv add langchain
uv add langchain-openai
uv add langgraph
uv add pydantic
```

or

```bash
pip install langchain langchain-openai langgraph pydantic
```

---

# Project Structure

```text
project/
│
├── main.py
├── tools.py
├── agents.py
├── README.md
│
└── .env
```

---

# Basic Agent

```python
from langchain.agents import create_agent

agent = create_agent(
    model=model,
    tools=[]
)
```

This creates a basic AI agent.

---

# Invoking The Agent

```python
response = agent.invoke(
    {
        "messages": [
            {
                "role": "user",
                "content": "Explain LangChain"
            }
        ]
    }
)

print(response)
```

---

# Creating Tools

Tools allow the agent to perform actions.

```python
from langchain.tools import tool

@tool
def search(query: str) -> str:
    """Search information"""
    return f"Results for: {query}"
```

---

# Agent With Tools

```python
agent = create_agent(
    model=model,
    tools=[search]
)
```

---

# System Prompt

System prompts define behavior.

```python
agent = create_agent(
    model=model,
    tools=[],
    system_prompt="""
    You are a senior Python mentor.
    Always explain step-by-step.
    """
)
```

---

# Structured Output

Useful when AI must return valid data.

```python
from pydantic import BaseModel

class Answer(BaseModel):
    summary: str
    confidence: float
```

```python
agent = create_agent(
    model=model,
    tools=[],
    response_format=Answer
)
```

Usage:

```python
result = agent.invoke(
    {
        "messages": [
            {
                "role": "user",
                "content": "Summarize LangChain"
            }
        ]
    }
)

print(result["structured_response"])
```

---

# Memory

Allows agents to remember conversations.

```python
from langgraph.checkpoint.memory import InMemorySaver

agent = create_agent(
    model=model,
    tools=[],
    checkpointer=InMemorySaver()
)
```

---

# Thread IDs

A thread ID identifies a conversation.

```python
config = {
    "configurable": {
        "thread_id": "demo-thread"
    }
}
```

Use the same thread ID to continue conversations.

---

# Memory Example

```python
response1 = agent.invoke(
    {
        "messages": [
            {
                "role": "user",
                "content": "My name is Dhiraj"
            }
        ]
    },
    config=config
)

response2 = agent.invoke(
    {
        "messages": [
            {
                "role": "user",
                "content": "What is my name?"
            }
        ]
    },
    config=config
)
```

---

# Context

Context allows additional runtime data.

```python
from dataclasses import dataclass

@dataclass
class Context:
    user_id: str
```

```python
agent = create_agent(
    model=model,
    tools=[],
    context_schema=Context
)
```

Usage:

```python
agent.invoke(
    {
        "messages": [
            {
                "role": "user",
                "content": "Hello"
            }
        ]
    },
    context=Context(
        user_id="user123"
    )
)
```

---

# Streaming

Generate tokens in real time.

```python
for chunk in agent.stream(
    {
        "messages": [
            {
                "role": "user",
                "content": "Explain LangChain"
            }
        ]
    }
):
    print(chunk)
```

---

# Retry Middleware

Automatically retries failures.

```python
from langchain.agents.middleware import (
    ModelRetryMiddleware
)

agent = create_agent(
    model=model,
    tools=[],
    middleware=[
        ModelRetryMiddleware(
            max_retries=3
        )
    ]
)
```

---

# PII Protection

Protect sensitive information.

```python
from langchain.agents.middleware import (
    PIIMiddleware
)

agent = create_agent(
    model=model,
    tools=[],
    middleware=[
        PIIMiddleware("email")
    ]
)
```

---

# Human In The Loop

Require approval before actions.

```python
from langchain.agents.middleware import (
    HumanInTheLoopMiddleware
)

agent = create_agent(
    model=model,
    tools=[],
    middleware=[
        HumanInTheLoopMiddleware(
            interrupt_on={
                "write_file": True
            }
        )
    ]
)
```

---

# Naming Agents

Useful in multi-agent systems.

```python
agent = create_agent(
    model=model,
    tools=[],
    name="research_assistant"
)
```

---

# Complete Working Example

```python
from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
from langchain.tools import tool

@tool
def search(query: str) -> str:
    """Search for information"""
    return f"Results for: {query}"

model = ChatOpenAI(
    api_key="YOUR_HF_TOKEN",
    base_url="https://router.huggingface.co/v1",
    model="meta-llama/Llama-3.1-8B-Instruct:novita",
    temperature=0.7,
)

agent = create_agent(
    model=model,
    tools=[search],
    system_prompt="""
    You are a helpful AI assistant.
    """
)

response = agent.invoke(
    {
        "messages": [
            {
                "role": "user",
                "content": "Search Python and explain it"
            }
        ]
    }
)

print(response)
```

---

# Learning Roadmap

Learn these topics in order:

## Level 1

* ChatOpenAI
* Messages
* invoke()

## Level 2

* create_agent()
* Tools
* System Prompts

## Level 3

* Memory
* thread_id
* Checkpointer

## Level 4

* Structured Output
* Streaming
* Context

## Level 5

* Middleware
* Guardrails
* Human In The Loop

## Level 6

* Subagents
* LangGraph
* Multi-Agent Systems

---

# Important Concepts

| Concept           | Meaning                           |
| ----------------- | --------------------------------- |
| Model             | AI brain                          |
| Agent             | Model + Tools + Memory            |
| Tool              | Function agent can use            |
| Thread ID         | Conversation ID                   |
| Checkpointer      | Saves conversations               |
| Context           | Runtime data                      |
| Middleware        | Agent customization               |
| Structured Output | Fixed response schema             |
| Streaming         | Real-time generation              |
| Subagent          | Agent controlled by another agent |

#
