# FastAPI Complete Guide

## Introduction

FastAPI is a modern, high-performance Python web framework for building APIs. It is designed to be easy to use, fast to develop with, and production-ready.

FastAPI is built on:

* Starlette (for web functionality)
* Pydantic (for data validation)

FastAPI leverages Python type hints to provide automatic request validation, serialization, and API documentation.

---

# Why FastAPI?

Traditional API frameworks often require:

* Manual validation
* Additional documentation tools
* Extra serialization logic

FastAPI provides:

* Automatic validation
* Automatic documentation
* Type safety
* High performance
* Async support

---

# Installation

Using pip:

```bash
pip install fastapi uvicorn
```

Using uv:

```bash
uv add fastapi uvicorn
```

Verify installation:

```bash
pip show fastapi
```

---

# Your First FastAPI Application

Create a file named `main.py`:

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {
        "message": "Hello FastAPI"
    }
```

Run the application:

```bash
uvicorn main:app --reload
```

Output:

```text
INFO: Uvicorn running on http://127.0.0.1:8000
```

Visit:

```text
http://127.0.0.1:8000
```

Response:

```json
{
    "message": "Hello FastAPI"
}
```

---

# Understanding FastAPI Components

## FastAPI Instance

```python
app = FastAPI()
```

Creates the application object.

---

## Route Decorators

```python
@app.get("/")
```

Defines a GET endpoint.

Available decorators:

```python
@app.get()
@app.post()
@app.put()
@app.patch()
@app.delete()
```

---

# HTTP Methods

| Method | Purpose        |
| ------ | -------------- |
| GET    | Retrieve data  |
| POST   | Create data    |
| PUT    | Replace data   |
| PATCH  | Partial update |
| DELETE | Remove data    |

---

# GET Request Example

```python
@app.get("/users")
def get_users():
    return [
        {"id": 1, "name": "John"},
        {"id": 2, "name": "Alice"}
    ]
```

---

# Path Parameters

```python
@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {
        "user_id": user_id
    }
```

Request:

```text
/users/10
```

Response:

```json
{
    "user_id": 10
}
```

FastAPI automatically converts and validates data types.

---

# Query Parameters

```python
@app.get("/search")
def search(q: str):
    return {
        "query": q
    }
```

Request:

```text
/search?q=python
```

Response:

```json
{
    "query": "python"
}
```

---

# Request Body

FastAPI uses Pydantic models.

```python
from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int
```

POST endpoint:

```python
@app.post("/users")
def create_user(user: User):
    return user
```

Request:

```json
{
    "name": "John",
    "age": 25
}
```

---

# Automatic Validation

Invalid request:

```json
{
    "name": "John",
    "age": "abc"
}
```

FastAPI automatically returns validation errors.

No manual validation code required.

---

# Response Models

```python
from pydantic import BaseModel

class UserResponse(BaseModel):
    id: int
    name: str
```

```python
@app.get(
    "/user",
    response_model=UserResponse
)
def get_user():
    return {
        "id": 1,
        "name": "John"
    }
```

---

# Automatic Documentation

FastAPI automatically generates documentation.

Swagger UI:

```text
http://127.0.0.1:8000/docs
```

ReDoc:

```text
http://127.0.0.1:8000/redoc
```

Features:

* Interactive testing
* Request examples
* Response schemas

---

# Async Support

FastAPI supports asynchronous endpoints.

```python
@app.get("/async")
async def async_route():
    return {
        "message": "Async API"
    }
```

Benefits:

* Better concurrency
* Improved scalability
* Efficient I/O operations

---

# CRUD API Example

## In-Memory Storage

```python
from fastapi import FastAPI

app = FastAPI()

users = []
```

---

## Create

```python
@app.post("/users")
def create_user(user: dict):
    users.append(user)
    return user
```

---

## Read

```python
@app.get("/users")
def get_users():
    return users
```

---

## Update

```python
@app.put("/users/{index}")
def update_user(
    index: int,
    user: dict
):
    users[index] = user
    return user
```

---

## Delete

```python
@app.delete("/users/{index}")
def delete_user(index: int):
    return {
        "deleted": users.pop(index)
    }
```

---

# FastAPI with MongoDB

Install MongoDB driver:

```bash
pip install pymongo
```

Connection:

```python
from pymongo import MongoClient

client = MongoClient(
    "mongodb://localhost:27017"
)

db = client.companyDB

collection = db.employees
```

Insert:

```python
collection.insert_one({
    "name": "John",
    "age": 25
})
```

Read:

```python
collection.find()
```

Update:

```python
collection.update_one(
    {"name": "John"},
    {
        "$set": {
            "age": 26
        }
    }
)
```

Delete:

```python
collection.delete_one(
    {"name": "John"}
)
```

---

# APIRouter

Used to organize routes.

Example:

```python
from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def home():
    return {
        "message": "Users Route"
    }
```

Register:

```python
app.include_router(
    router,
    prefix="/users"
)
```

---

# Dependency Injection

Example:

```python
from fastapi import Depends

def get_db():
    return "Database"

@app.get("/")
def home(
    db=Depends(get_db)
):
    return db
```

Benefits:

* Cleaner code
* Easier testing
* Reusable dependencies

---

# Middleware

Middleware runs before and after requests.

Example:

```python
from fastapi import Request

@app.middleware("http")
async def logger(
    request: Request,
    call_next
):
    response = await call_next(request)
    return response
```

Common uses:

* Logging
* Authentication
* Rate limiting

---

# Exception Handling

```python
from fastapi import HTTPException

@app.get("/users/{id}")
def get_user(id: int):

    if id != 1:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return {
        "id": id
    }
```

---

# Environment Variables

Install:

```bash
pip install python-dotenv
```

Example `.env`:

```text
MONGO_URI=mongodb://localhost:27017
SECRET_KEY=mysecret
```

Load:

```python
from dotenv import load_dotenv
import os

load_dotenv()

mongo_uri = os.getenv(
    "MONGO_URI"
)
```

---

# Project Structure

```text
fastapi_project/
│
├── app/
│   ├── main.py
│   ├── routes/
│   │   └── users.py
│   ├── models/
│   │   └── user.py
│   ├── database/
│   │   └── connection.py
│   └── services/
│
├── .env
├── requirements.txt
└── README.md
```

---

# FastAPI vs Flask

| Feature       | Flask          | FastAPI      |
| ------------- | -------------- | ------------ |
| Performance   | Good           | Excellent    |
| Async Support | Limited        | Built-in     |
| Validation    | Manual         | Automatic    |
| Swagger Docs  | Extra packages | Built-in     |
| Type Hints    | Optional       | Core Feature |

---

# Advantages of FastAPI

* High performance
* Automatic documentation
* Async support
* Automatic validation
* Type-safe development
* Easy testing
* Modern architecture

---

# Real-World Use Cases

* AI Applications
* LangChain APIs
* RAG Systems
* Chatbots
* SaaS Platforms
* Mobile Backends
* Authentication Services
* E-commerce APIs

---

# Common Interview Questions

### What is FastAPI?

FastAPI is a modern Python framework for building APIs using type hints, automatic validation, and asynchronous programming.

---

### Why is FastAPI fast?

Because it uses:

* Starlette
* ASGI
* Async support

---

### What is Pydantic?

Pydantic validates and serializes data using Python type hints.

---

### What is Uvicorn?

Uvicorn is an ASGI server used to run FastAPI applications.

Example:

```bash
uvicorn main:app --reload
```

---

### What is Dependency Injection?

A mechanism for providing dependencies automatically using `Depends()`.

---

### What are Middleware Components?

Middleware executes before and after requests for tasks such as logging and authentication.

---

# Interview Definition

FastAPI is a modern, high-performance Python web framework used for building APIs. It leverages Python type hints, Pydantic-based validation, asynchronous programming, and automatic API documentation to simplify backend development and improve performance.
