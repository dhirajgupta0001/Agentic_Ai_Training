# LangChain Middleware Explained

Middleware in LangChain allows you to **intercept and customize an agent's execution** without modifying the agent's core logic. It lets you execute your own code **before**, **after**, or **around** model and tool calls.

---

# Agent Execution Flow

Think of an agent like this:

```text
User
  ↓
before_agent
  ↓
before_model
  ↓
wrap_model_call
  ↓
LLM
  ↓
after_model
  ↓
Need tool?
     ↓
wrap_tool_call
     ↓
Tool
     ↓
after_agent
  ↓
Final Response
```

Each middleware hook allows you to customize a specific stage of the execution.

---

# 1. Node-Style Hooks

Node-style hooks run at **specific execution points**.

They are mainly used for:

- Logging
- Validation
- State updates
- Permission checks
- Ending execution early

## Available Hooks

| Hook | Runs When |
|------|-----------|
| `before_agent` | Before the agent starts |
| `before_model` | Before every LLM call |
| `after_model` | After every LLM response |
| `after_agent` | After the agent finishes |

## Example: before_model

```python
@before_model
def check_limit(state, runtime):
    ...
```

This function executes **before** the model is called.

It can:

- Inspect conversation messages
- Modify agent state
- Stop execution
- Redirect execution using `jump_to`

Example:

```python
@before_model
def check_limit(state, runtime):
    if len(state["messages"]) > 50:
        return {"jump_to": "end"}
```

---

## Example: after_model

```python
@after_model
def log_response(state, runtime):
    print(state["messages"][-1])
```

This executes immediately **after** the LLM returns a response.

Common uses:

- Logging
- Analytics
- Tracking token usage
- Updating custom state

---

# 2. Wrap-Style Hooks

Wrap-style hooks wrap the **actual model or tool call**.

Instead of simply executing before or after something, they surround the call.

Instead of:

```text
Model
```

it becomes

```text
Your Code
    ↓
handler()   ← Actual Model Call
    ↓
Your Code
```

The important part is:

```python
handler()
```

`handler()` is the actual LLM or tool execution.

Your middleware decides:

- Whether to call it
- When to call it
- How many times to call it

---

## Example: Retry Middleware

```python
@wrap_model_call
def retry(request, handler):
    try:
        return handler(request)
    except:
        return handler(request)
```

Here the middleware retries the model call if the first attempt fails.

---

# Why Wrap Hooks Are Powerful

Since you control `handler()`, you can:

- Retry failed requests
- Cache responses
- Change prompts
- Select different models
- Skip model execution entirely
- Modify requests before execution
- Modify responses after execution

---

# Real Example: Dynamic Model Selection

Suppose your application has two models.

```text
Simple Question
        ↓
Middleware
        ↓
GPT-5-mini

Complex Question
        ↓
Middleware
        ↓
GPT-5
```

Example:

```python
@wrap_model_call
def dynamic_model(request, handler):

    if len(request.messages) > 10:
        request = request.override(model=complex_model)
    else:
        request = request.override(model=simple_model)

    return handler(request)
```

The middleware decides **which model** should answer the request.

---

# Real Example: Tool Monitoring

```text
Agent
   ↓
Middleware
   ↓
Calculator Tool
   ↓
Middleware logs:
"Calculator called with x = 5"
```

Example:

```python
@wrap_tool_call
def monitor(request, handler):

    print(request.tool_call["name"])

    result = handler(request)

    print("Tool completed")

    return result
```

The middleware observes the tool execution without changing the tool itself.

---

# The Big Picture

Suppose you create an agent like this:

```python
agent = create_agent(
    model=model,
    tools=tools,
    middleware=[
        LoggingMiddleware(),
        RetryMiddleware(),
        DynamicModelMiddleware(),
    ]
)
```

The agent itself only focuses on solving the user's problem.

Each middleware has a single responsibility.

### Logging Middleware

- Logs requests
- Logs responses
- Records execution information

### Retry Middleware

- Retries failed model calls
- Retries failed tool calls

### Dynamic Model Middleware

- Chooses the best model
- Routes simple requests to smaller models
- Routes difficult requests to larger models

### Safety Middleware

- Blocks unsafe prompts
- Filters harmful outputs

### Caching Middleware

- Returns cached responses
- Avoids unnecessary LLM calls

---

# Difference Between Node Hooks and Wrap Hooks

| Node Hooks | Wrap Hooks |
|------------|------------|
| Execute before or after a step | Surround the execution |
| Cannot control how many times the model runs | Can call the model multiple times |
| Best for logging and validation | Best for retries, caching, routing |
| Simpler | More powerful |

---

# Key Takeaway

Middleware in LangChain is a mechanism for injecting custom behavior into an agent's execution pipeline.

- **Node-style hooks** execute at fixed points (before/after the agent or model).
- **Wrap-style hooks** surround model or tool calls and give you complete control over execution.
- Middleware keeps the agent's core logic clean by handling cross-cutting concerns such as logging, retries, caching, dynamic model selection, safety checks, and monitoring separately.
