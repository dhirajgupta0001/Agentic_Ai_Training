# Uvicorn Complete Guide

## Introduction

Uvicorn is a lightweight, high-performance ASGI (Asynchronous Server Gateway Interface) server used to run modern Python web applications.

It is commonly used with:

* FastAPI
* Starlette
* Quart
* Other ASGI-compatible frameworks

Uvicorn acts as the bridge between client requests and your Python application.

---

# Why Do We Need Uvicorn?

Consider a FastAPI application:

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {
        "message": "Hello FastAPI"
    }
```

This code only defines the application.

To make it accessible through a browser, you need a server.

That server is Uvicorn.

```bash
uvicorn main:app
```

Uvicorn starts a web server and serves the FastAPI application.

---

# What is ASGI?

ASGI stands for:

```text
Asynchronous Server Gateway Interface
```

It is the modern replacement for WSGI.

---

# WSGI vs ASGI

## WSGI Architecture

```text
Browser
   │
   ▼
WSGI Server
(Gunicorn)
   │
   ▼
Flask / Django
```

WSGI is synchronous.

---

## ASGI Architecture

```text
Browser
   │
   ▼
ASGI Server
(Uvicorn)
   │
   ▼
FastAPI
```

ASGI supports:

* Async programming
* WebSockets
* Long-lived connections
* High concurrency

---

# Features of Uvicorn

* Lightweight
* Fast
* Async support
* WebSocket support
* HTTP/1.1 support
* ASGI compliant
* Production-ready

---

# Installing Uvicorn

Using pip:

```bash
pip install uvicorn
```

Using uv:

```bash
uv add uvicorn
```

Install with FastAPI:

```bash
pip install fastapi uvicorn
```

---

# Basic FastAPI Application

Create `main.py`:

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {
        "message": "Hello World"
    }
```

---

# Running the Application

Start Uvicorn:

```bash
uvicorn main:app
```

Where:

```text
main  → main.py
app   → FastAPI instance
```

Output:

```text
INFO: Uvicorn running on http://127.0.0.1:8000
```

---

# Accessing the Application

Open browser:

```text
http://127.0.0.1:8000
```

Response:

```json
{
    "message": "Hello World"
}
```

---

# Auto Reload Mode

During development:

```bash
uvicorn main:app --reload
```

Benefits:

* Automatically reloads on file changes
* Faster development workflow
* No manual restart required

---

# Custom Host

Default:

```text
127.0.0.1
```

To allow external access:

```bash
uvicorn main:app --host 0.0.0.0
```

Now accessible from:

```text
http://YOUR_IP:8000
```

---

# Custom Port

Default port:

```text
8000
```

Custom port:

```bash
uvicorn main:app --port 9000
```

Access:

```text
http://localhost:9000
```

---

# Host and Port Together

```bash
uvicorn main:app --host 0.0.0.0 --port 9000
```

---

# Understanding main

Example:

```python
# main.py

from fastapi import FastAPI

app = FastAPI()
```

Command:

```bash
uvicorn main:app
```

Explanation:

```text
main → Python filename
app  → FastAPI object
```

Format:

```text
uvicorn <module>:<application>
```

---

# Request Flow

```text
Browser
   │
GET /
   │
   ▼
Uvicorn
   │
   ▼
FastAPI
   │
   ▼
JSON Response
```

---

# How Uvicorn Works Internally

When started:

```bash
uvicorn main:app --reload
```

Uvicorn:

1. Imports `main.py`
2. Finds the `app` object
3. Creates an ASGI server
4. Listens for requests
5. Sends requests to FastAPI
6. Returns responses to clients

---

# Running with Python

Instead of:

```bash
uvicorn main:app
```

You can run:

```python
import uvicorn

uvicorn.run(
    "main:app",
    host="127.0.0.1",
    port=8000,
    reload=True
)
```

---

# WebSocket Support

One major advantage of Uvicorn is native WebSocket support.

Example:

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
            f"Echo: {data}"
        )
```

Run:

```bash
uvicorn main:app --reload
```

Uvicorn manages the WebSocket connection.

---

# Async Support

FastAPI endpoint:

```python
@app.get("/")
async def home():
    return {
        "message": "Async"
    }
```

Because Uvicorn is ASGI-based:

* Multiple requests can be handled concurrently
* Better scalability
* Improved performance

---

# Logging

Default logs:

```text
INFO: Started server process
INFO: Waiting for application startup
INFO: Application startup complete
INFO: Uvicorn running on http://127.0.0.1:8000
```

---

# Production Deployment

For production, many teams use:

```bash
gunicorn -k uvicorn.workers.UvicornWorker main:app
```

Architecture:

```text
Gunicorn
   │
   ├── Worker 1 (Uvicorn)
   ├── Worker 2 (Uvicorn)
   ├── Worker 3 (Uvicorn)
   └── Worker 4 (Uvicorn)
```

Benefits:

* Multiple processes
* Better reliability
* Improved scaling

---

# Uvicorn vs Gunicorn

| Feature         | Uvicorn   | Gunicorn |
| --------------- | --------- | -------- |
| Server Type     | ASGI      | WSGI     |
| Async Support   | Yes       | No       |
| WebSockets      | Yes       | No       |
| FastAPI Support | Excellent | Limited  |
| Performance     | High      | Good     |

---

# Uvicorn vs Hypercorn

| Feature           | Uvicorn   | Hypercorn |
| ----------------- | --------- | --------- |
| ASGI Support      | Yes       | Yes       |
| WebSocket Support | Yes       | Yes       |
| HTTP/2 Support    | Limited   | Better    |
| Popularity        | Very High | Moderate  |

---

# Common Commands

### Development

```bash
uvicorn main:app --reload
```

### Production

```bash
uvicorn main:app
```

### Custom Host

```bash
uvicorn main:app --host 0.0.0.0
```

### Custom Port

```bash
uvicorn main:app --port 8080
```

### Host + Port

```bash
uvicorn main:app --host 0.0.0.0 --port 8080
```

---

# Typical FastAPI Project

```text
project/
│
├── main.py
├── routes/
├── models/
├── services/
├── requirements.txt
└── .env
```

Run:

```bash
uvicorn main:app --reload
```

---

# Advantages of Uvicorn

* Fast performance
* Low memory usage
* Native async support
* WebSocket support
* Excellent FastAPI integration
* Easy deployment

---

# Common Interview Questions

## What is Uvicorn?

Uvicorn is a lightweight ASGI server used to run FastAPI and other asynchronous Python web applications.

---

## Why is Uvicorn used with FastAPI?

Because FastAPI is built on ASGI and requires an ASGI server to process requests.

---

## What does `main:app` mean?

```text
main → Python file (main.py)
app  → FastAPI application instance
```

---

## What is ASGI?

ASGI (Asynchronous Server Gateway Interface) is the modern Python standard for asynchronous web applications and servers.

---

## Does Uvicorn support WebSockets?

Yes.

Uvicorn supports:

* HTTP
* WebSockets
* Async applications

---

## Difference Between FastAPI and Uvicorn?

| FastAPI        | Uvicorn          |
| -------------- | ---------------- |
| Framework      | Server           |
| Defines APIs   | Runs APIs        |
| Handles routes | Handles requests |

---

# Interview Definition

Uvicorn is a high-performance ASGI server used to run asynchronous Python web applications such as FastAPI. It supports HTTP, WebSockets, and asynchronous request handling, making it a popular choice for modern API development.
