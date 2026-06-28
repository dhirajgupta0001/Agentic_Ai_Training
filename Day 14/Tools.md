# LangChain Tools – Summary Notes

# LangChain Tools

## What are Tools?

**Tools** are functions that extend the capabilities of an LLM by allowing it to interact with external systems. Instead of only generating text from its training data, the model can call tools to retrieve information, execute code, or perform actions.

### Examples

* Search the web
* Query databases
* Execute Python code
* Read or write files
* Call REST APIs
* Access memory
* Perform calculations

---

# Why are Tools Needed?

LLMs have limitations:

* No access to real-time information
* Cannot execute code on their own
* Cannot directly interact with databases or APIs
* Cannot remember information across sessions without memory

Tools solve these limitations by allowing the model to interact with external resources.

---

# How Tool Calling Works

```
User
   │
   ▼
LLM receives request
   │
   ▼
Decides a tool is needed
   │
   ▼
Calls the tool
   │
   ▼
Tool executes
   │
   ▼
Returns result
   │
   ▼
LLM generates final response
```

---

# Creating a Tool

Use the `@tool` decorator.

```python
from langchain.tools import tool

@tool
def search_database(query: str) -> str:
    """Search customer database."""
    return f"Results for {query}"
```

### Requirements

* Type hints are required.
* A meaningful docstring is recommended.
* Function name becomes the tool name by default.

---

# Tool Components

Every tool consists of:

* Tool Name
* Description
* Input Schema
* Function Logic
* Output

---

# Customizing Tools

## Custom Tool Name

```python
@tool("web_search")
def search(query: str):
    ...
```

## Custom Description

```python
@tool(
    "calculator",
    description="Use this tool for arithmetic calculations."
)
```

---

# Input Schemas

## Basic Type Hints

```python
def weather(city: str):
```

## Pydantic Schema

```python
class WeatherInput(BaseModel):
    city: str
    units: str
```

Benefits:

* Input validation
* Better documentation
* Supports complex inputs

---

# Reserved Argument Names

Avoid using these parameter names:

* `config`
* `runtime`

These are reserved internally by LangChain.

---

# ToolRuntime

`ToolRuntime` gives tools access to runtime information.

It provides:

* State
* Context
* Store
* Stream Writer
* Execution Info
* Server Info
* Tool Call ID

---

# State (Short-Term Memory)

State exists only during the current conversation.

Examples:

* Conversation history
* Counters
* Temporary variables

```python
runtime.state["messages"]
```

---

# Context

Context contains immutable information passed when invoking the agent.

Examples:

* user_id
* session_id
* account type

```python
runtime.context.user_id
```

---

# Store (Long-Term Memory)

Store keeps information across conversations.

Examples:

* User preferences
* Saved profile
* Persistent memory

```python
runtime.store.get(...)
runtime.store.put(...)
```

---

# Stream Writer

Used to send progress updates while a tool is running.

```python
runtime.stream_writer("Downloading...")
```

Useful for long-running operations.

---

# Execution Info

Provides execution metadata such as:

* Thread ID
* Run ID
* Retry Count

Useful for debugging.

---

# Server Info

Available only on LangGraph Server.

Contains:

* Assistant ID
* Graph ID
* Authenticated User

---

# Tool Return Types

## 1. String

```python
return "Weather is sunny."
```

Used for human-readable responses.

---

## 2. Object

```python
return {
    "temperature":22,
    "condition":"Sunny"
}
```

Useful for structured data.

---

## 3. Multimodal Content

Return text together with images or other media.

---

## 4. Command

Used when updating the graph state.

---

# return_direct=True

```python
@tool(return_direct=True)
```

The tool output is returned directly to the user without another LLM call.

Use this when the tool already provides the final answer.

---

# Error Handling

LangChain supports middleware for handling tool failures.

Benefits:

* Prevent crashes
* Retry failed calls
* Return friendly error messages

---

# Dynamic Tool Selection

The available tools can change depending on:

* User authentication
* User permissions
* Conversation state
* Feature flags

Advantages:

* Better security
* Smaller context
* Improved performance

---

# Headless Tools

Headless tools execute outside the server, typically in the user's browser.

Common uses:

* Clipboard access
* Geolocation
* File picker
* Browser APIs
* Canvas operations

---

# Prebuilt Tools

LangChain offers many ready-to-use integrations, including:

* Web Search
* SQL Databases
* Python REPL
* Vector Stores
* GitHub
* Gmail
* Slack
* Notion
* Retrieval Systems

---

# Server-Side Tools

Some LLM providers include built-in tools such as:

* Web Search
* Code Interpreter

These execute on the provider's infrastructure instead of your application.

---

# Best Practices

* Use descriptive tool names.
* Write clear docstrings.
* Keep each tool focused on a single task.
* Use Pydantic for complex inputs.
* Validate user inputs.
* Handle exceptions properly.
* Prefer `snake_case` names.
* Use `return_direct=True` only when appropriate.

---

# Common Tool Types

| Tool Type       | Purpose                               |
| --------------- | ------------------------------------- |
| Search Tool     | Search the web                        |
| Database Tool   | Query SQL/NoSQL databases             |
| API Tool        | Call external APIs                    |
| File Tool       | Read or write files                   |
| Memory Tool     | Save and retrieve user information    |
| Calculator Tool | Perform arithmetic                    |
| Python Tool     | Execute Python code                   |
| Retrieval Tool  | Retrieve documents from vector stores |

---

# Quick Cheat Sheet

| Concept              | Purpose                           |
| -------------------- | --------------------------------- |
| `@tool`              | Create a tool                     |
| Type Hints           | Define input schema               |
| Docstring            | Explains tool usage               |
| `ToolRuntime`        | Access runtime information        |
| State                | Short-term memory                 |
| Context              | Immutable runtime data            |
| Store                | Long-term memory                  |
| Stream Writer        | Progress updates                  |
| `return_direct=True` | Return tool output immediately    |
| Middleware           | Handle tool errors                |
| Headless Tool        | Runs on the client/browser        |
| Dynamic Tools        | Change available tools at runtime |

---

# Summary

LangChain Tools allow an LLM to interact with external systems such as APIs, databases, files, memory, and web services. A tool is created using the `@tool` decorator, includes an input schema, and returns data back to the model. Advanced features such as `ToolRuntime`, memory access, streaming, dynamic tool selection, and error handling make tools powerful building blocks for creating intelligent AI agents.
