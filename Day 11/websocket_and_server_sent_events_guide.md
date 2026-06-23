# WebSockets and Server-Sent Events (SSE) in Python & FastAPI

## Introduction

Modern applications often require real-time communication between clients and servers.

Examples:

* Chat applications
* Live notifications
* Stock market dashboards
* Online gaming
* Monitoring systems
* AI streaming responses

Traditional HTTP communication is request-response based and is not ideal for real-time updates.

To solve this problem, developers use:

1. WebSockets
2. Server-Sent Events (SSE)

---

# Traditional HTTP Communication

HTTP follows a request-response model:

```text
Client  ---> Request ---> Server
Client <--- Response <--- Server
```

After the response is sent, the connection is closed.

If a client needs updates continuously, it must repeatedly ask the server:

```text
Client:
"Any updates?"

Server:
"No."

Client:
"Any updates now?"

Server:
"No."
```

This process is called polling and is inefficient.

---

# What is WebSocket?

WebSocket is a protocol that provides a persistent, bidirectional communication channel between a client and a server.

Unlike HTTP:

```text
Client <=================> Server
      Full Duplex
```

Both sides can send and receive data at any time.

---

# WebSocket Lifecycle

```text
Client
   │
   ▼
HTTP Request
   │
   ▼
Protocol Upgrade
   │
   ▼
WebSocket Connection
   │
   ▼
Real-Time Communication
```

Once established, the connection remains open.

---

# Features of WebSockets

* Persistent connection
* Full duplex communication
* Low latency
* Real-time messaging
* Efficient network usage

---

# FastAPI WebSocket Example

Create a FastAPI application:

```python
from fastapi import FastAPI, WebSocket

app = FastAPI()

@app.websocket("/ws")
async def websocket_endpoint(
    websocket: WebSocket
):
    await websocket.accept()

    while True:

        data = await websocket.receive_text()

        await websocket.send_text(
            f"You sent: {data}"
        )
```

Run:

```bash
uvicorn main:app --reload
```

---

# JavaScript WebSocket Client

```javascript
const ws = new WebSocket(
    "ws://localhost:8000/ws"
);

ws.onmessage = (event) => {
    console.log(event.data);
};

ws.send("Hello Server");
```

---

# WebSocket Message Flow

```text
Client
   │
   ├── Hello
   │
   ▼
Server
   │
   ├── You sent: Hello
   │
   ▼
Client
```

---

# Building a Chat Application

WebSockets are commonly used for chat systems.

Example:

```text
User A
   │
   ▼
Server
   │
   ▼
User B
```

Messages can flow in both directions instantly.

---

# FastAPI Chat Example

```python
from fastapi import FastAPI, WebSocket

app = FastAPI()

connections = []

@app.websocket("/chat")
async def chat(
    websocket: WebSocket
):
    await websocket.accept()

    connections.append(websocket)

    while True:

        message = await websocket.receive_text()

        for connection in connections:
            await connection.send_text(
                message
            )
```

This creates a simple chat room.

---

# WebSocket Use Cases

## Chat Applications

Examples:

* WhatsApp
* Slack
* Discord

---

## Multiplayer Games

```text
Player Action
      ↓
WebSocket
      ↓
Live Updates
```

---

## Trading Platforms

```text
Stock Prices
      ↓
WebSocket
      ↓
Browser
```

---

## Collaborative Editing

Examples:

* Google Docs
* Figma

---

# Advantages of WebSockets

* Real-time communication
* Low latency
* Reduced overhead
* Efficient for frequent updates

---

# Disadvantages of WebSockets

* More complex implementation
* Requires connection management
* Scaling can be challenging

---

# What are Server-Sent Events (SSE)?

Server-Sent Events allow servers to push updates to clients over a persistent HTTP connection.

Communication is one-way:

```text
Server ─────────► Client
```

The client cannot send messages through the SSE connection.

---

# SSE Lifecycle

```text
Client Connects
        │
        ▼
Connection Stays Open
        │
        ▼
Server Pushes Events
        │
        ▼
Client Receives Events
```

---

# Features of SSE

* Simple implementation
* HTTP-based
* Automatic reconnection
* Lightweight
* Ideal for server-to-client streaming

---

# FastAPI SSE Setup

Install:

```bash
pip install sse-starlette
```

---

# FastAPI SSE Example

```python
from fastapi import FastAPI
from sse_starlette.sse import EventSourceResponse

import asyncio

app = FastAPI()

@app.get("/events")
async def events():

    async def generator():

        while True:

            yield {
                "data": "Hello Client"
            }

            await asyncio.sleep(2)

    return EventSourceResponse(
        generator()
    )
```

---

# JavaScript SSE Client

```javascript
const eventSource =
    new EventSource("/events");

eventSource.onmessage =
(event) => {
    console.log(event.data);
};
```

Output:

```text
Hello Client
Hello Client
Hello Client
```

Received every two seconds.

---

# SSE Data Flow

```text
Server
   │
   ▼
Event Stream
   │
   ▼
Client
```

Only the server sends updates.

---

# SSE Use Cases

## Notifications

```text
Server
   ↓
Notification
   ↓
Browser
```

Examples:

* New messages
* System alerts
* Status updates

---

## AI Response Streaming

```text
LLM
 ↓
Token Stream
 ↓
Browser
```

Many AI systems stream generated tokens using SSE.

---

## Monitoring Dashboards

Examples:

* CPU usage
* Memory usage
* Application logs

---

## Live Feeds

Examples:

* News updates
* Sports scores
* Market data

---

# WebSocket vs SSE

| Feature                    | WebSocket       | SSE            |
| -------------------------- | --------------- | -------------- |
| Communication              | Bidirectional   | Unidirectional |
| Client → Server            | Yes             | No             |
| Server → Client            | Yes             | Yes            |
| Real-Time Updates          | Yes             | Yes            |
| Uses HTTP Connection       | Initial Upgrade | Entire Time    |
| Complexity                 | Higher          | Lower          |
| Automatic Reconnect        | Manual          | Built-in       |
| Suitable for Chat Apps     | Yes             | No             |
| Suitable for Notifications | Yes             | Yes            |

---

# Architecture Comparison

## WebSocket

```text
Client
   ⇅
WebSocket
   ⇅
Server
```

Two-way communication.

---

## SSE

```text
Client
   ▲
   │
SSE
   │
Server
```

One-way communication.

---

# FastAPI Real-Time Example

## WebSocket

```python
@app.websocket("/ws")
```

Best for:

* Chat apps
* Gaming
* Collaboration tools

---

## SSE

```python
@app.get("/events")
```

Best for:

* Notifications
* Dashboards
* AI streaming responses

---

# Choosing Between WebSocket and SSE

Use WebSocket when:

* Client and server both need to send data.
* Building chat applications.
* Implementing multiplayer games.
* Supporting collaborative editing.

Use SSE when:

* Only the server sends updates.
* Streaming AI responses.
* Sending notifications.
* Updating dashboards.

---

# Real-World Examples

| Application           | Technology |
| --------------------- | ---------- |
| WhatsApp              | WebSocket  |
| Slack                 | WebSocket  |
| Discord               | WebSocket  |
| ChatGPT Streaming     | SSE        |
| GitHub Notifications  | SSE        |
| Monitoring Dashboards | SSE        |

---

# Common Interview Questions

## What is WebSocket?

A protocol that enables persistent, bidirectional communication between a client and a server.

---

## What is SSE?

A technology that allows servers to continuously push updates to clients over HTTP.

---

## Why are WebSockets faster than polling?

Because the connection remains open and messages are exchanged instantly without repeated HTTP requests.

---

## Can SSE send data from client to server?

No.

SSE supports only:

```text
Server → Client
```

communication.

---

## Which is better for chat applications?

WebSocket.

Because chat applications require:

```text
Client ⇄ Server
```

communication.

---

## Which is better for AI token streaming?

SSE.

Because responses flow primarily:

```text
Server → Client
```

---

# Interview Definition

### WebSocket

WebSocket is a communication protocol that enables persistent, full-duplex communication between a client and a server over a single TCP connection.

### Server-Sent Events (SSE)

Server-Sent Events (SSE) is a technology that enables servers to push real-time updates to clients over a persistent HTTP connection, supporting one-way communication from server to client.
