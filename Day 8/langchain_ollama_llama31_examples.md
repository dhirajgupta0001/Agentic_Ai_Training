# LangChain + Ollama + Llama 3.1 Complete Examples

## Installation

```bash
pip install -U langchain langchain-ollama pydantic
```

Start Ollama:

```bash
ollama run llama3.1
```

---

# 1. Initialize Llama 3.1

```python
from langchain_ollama import ChatOllama

model = ChatOllama(
    model="llama3.1",
    temperature=0.7
)
```

---

# 2. Simple Invoke

```python
response = model.invoke(
    "Why do parrots talk?"
)

print(response.content)
```

---

# 3. Conversation Example

```python
from langchain_core.messages import (
    SystemMessage,
    HumanMessage,
    AIMessage
)

conversation = [
    SystemMessage(
        content="You are a French translator."
    ),
    HumanMessage(
        content="Translate: I love programming."
    ),
    AIMessage(
        content="J'adore la programmation."
    ),
    HumanMessage(
        content="Translate: I love building applications."
    )
]

response = model.invoke(conversation)

print(response.content)
```

---

# 4. Streaming

```python
for chunk in model.stream(
    "Explain quantum computing simply."
):
    print(
        chunk.content,
        end="",
        flush=True
    )
```

---

# 5. Batch Processing

```python
responses = model.batch([
    "What is Python?",
    "What is AI?",
    "What is LangChain?"
])

for response in responses:
    print(response.content)
```

---

# 6. Batch With Concurrency

```python
responses = model.batch(
    [
        "What is Python?",
        "What is AI?",
        "What is LangChain?"
    ],
    config={
        "max_concurrency": 3
    }
)

for response in responses:
    print(response.content)
```

---

# 7. Tool Calling Example

```python
from langchain_core.tools import tool

@tool
def get_weather(location: str) -> str:
    """Get weather information."""
    return f"Sunny in {location}"

model_with_tools = model.bind_tools(
    [get_weather]
)

response = model_with_tools.invoke(
    "What's the weather in Delhi?"
)

print(response.tool_calls)
```

---

# 8. Tool Execution Loop

```python
messages = [
    {
        "role": "user",
        "content": "What's the weather in Delhi?"
    }
]

ai_msg = model_with_tools.invoke(
    messages
)

messages.append(ai_msg)

for tool_call in ai_msg.tool_calls:
    result = get_weather.invoke(
        tool_call
    )
    messages.append(result)

final_response = model_with_tools.invoke(
    messages
)

print(final_response.content)
```

---

# 9. Force Tool Usage

```python
model_with_tools = model.bind_tools(
    [get_weather],
    tool_choice="get_weather"
)
```

---

# 10. Parallel Tool Calls

```python
response = model_with_tools.invoke(
    "What's the weather in Delhi and Mumbai?"
)

print(response.tool_calls)
```

---

# 11. Structured Output (Pydantic)

```python
from pydantic import BaseModel

class Movie(BaseModel):
    title: str
    year: int
    director: str
    rating: float

structured_model = (
    model.with_structured_output(
        Movie
    )
)

response = structured_model.invoke(
    "Tell me about Inception"
)

print(response)
```

---

# 12. Structured Output (TypedDict)

```python
from typing_extensions import TypedDict

class MovieDict(TypedDict):
    title: str
    year: int
    director: str
    rating: float

structured_model = (
    model.with_structured_output(
        MovieDict
    )
)

response = structured_model.invoke(
    "Tell me about Interstellar"
)

print(response)
```

---

# 13. Structured Output (JSON Schema)

```python
schema = {
    "title": "Movie",
    "type": "object",
    "properties": {
        "title": {
            "type": "string"
        },
        "year": {
            "type": "integer"
        },
        "director": {
            "type": "string"
        },
        "rating": {
            "type": "number"
        }
    }
}

structured_model = (
    model.with_structured_output(
        schema
    )
)

response = structured_model.invoke(
    "Tell me about Inception"
)

print(response)
```

---

# 14. Multimodal Image Input

Requires a vision-capable model such as:

```bash
ollama run llama3.2-vision
```

```python
import base64

with open(
    "image.jpg",
    "rb"
) as file:
    image_data = (
        base64.b64encode(
            file.read()
        ).decode()
    )

message = [
    {
        "role": "user",
        "content": [
            {
                "type": "text",
                "text": "Describe this image"
            },
            {
                "type": "image_url",
                "image_url":
                f"data:image/jpeg;base64,{image_data}"
            }
        ]
    }
]

response = model.invoke(
    message
)

print(response.content)
```

---

# 15. Runtime Configuration

```python
from langchain.chat_models import (
    init_chat_model
)

configurable_model = (
    init_chat_model(
        temperature=0
    )
)

response = configurable_model.invoke(
    "Hello",
    config={
        "configurable": {
            "model": "llama3.1"
        }
    }
)

print(response.content)
```

---

# 16. Token Usage

```python
response = model.invoke(
    "Explain LangChain."
)

print(
    response.response_metadata
)
```

---

# 17. Rate Limiter

```python
from langchain_core.rate_limiters import (
    InMemoryRateLimiter
)

rate_limiter = (
    InMemoryRateLimiter(
        requests_per_second=1,
        check_every_n_seconds=0.1,
        max_bucket_size=5
    )
)

model = ChatOllama(
    model="llama3.1",
    rate_limiter=rate_limiter
)
```

---

# 18. Complete Minimal Working Example

```python
from langchain_ollama import (
    ChatOllama
)

model = ChatOllama(
    model="llama3.1",
    temperature=0.7
)

response = model.invoke(
    "Explain LangChain in simple terms"
)

print(response.content)
```

#
