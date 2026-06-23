# HTTP Status Codes Complete Guide

## Introduction

HTTP Status Codes are three-digit numbers returned by a server in response to a client's request.

They tell the client whether the request was successful, redirected, invalid, or failed.

Example:

```http
GET /users HTTP/1.1

HTTP/1.1 200 OK
```

Here:

```text
200 = Success
```

---

# Why Status Codes Matter

When a browser, mobile app, or API sends a request:

```text
Client
   │
Request
   ▼
Server
   │
Response + Status Code
   ▼
Client
```

The status code helps determine what happened.

Example:

```text
200 → Success
404 → Resource Not Found
500 → Server Error
```

---

# Categories of HTTP Status Codes

| Range   | Category      |
| ------- | ------------- |
| 100-199 | Informational |
| 200-299 | Success       |
| 300-399 | Redirection   |
| 400-499 | Client Errors |
| 500-599 | Server Errors |

---

# 1xx Informational Responses

These indicate that the request has been received and processing continues.

---

## 100 Continue

```http
HTTP/1.1 100 Continue
```

Meaning:

```text
Request received.
Continue sending data.
```

---

## 101 Switching Protocols

Used for WebSockets.

```http
HTTP/1.1 101 Switching Protocols
```

Example:

```text
HTTP → WebSocket Upgrade
```

---

# 2xx Success Responses

The request completed successfully.

---

## 200 OK

Most common success response.

```http
HTTP/1.1 200 OK
```

Example:

```python
@app.get("/users")
def get_users():
    return users
```

Response:

```text
200 OK
```

---

## 201 Created

Resource created successfully.

Example:

```python
@app.post("/users")
def create_user():
    ...
```

Response:

```text
201 Created
```

Common in:

* User creation
* Product creation
* Database inserts

---

## 202 Accepted

Request accepted for processing.

```text
202 Accepted
```

Used for:

* Background jobs
* Queue processing

---

## 204 No Content

Success but no response body.

```text
204 No Content
```

Example:

```python
@app.delete("/users/1")
```

---

# 3xx Redirection Responses

The client must take additional action.

---

## 301 Moved Permanently

```text
301 Moved Permanently
```

Example:

```text
oldsite.com
     ↓
newsite.com
```

Search engines update their indexes.

---

## 302 Found

Temporary redirect.

```text
302 Found
```

Used when a page is temporarily moved.

---

## 304 Not Modified

Used for caching.

```text
304 Not Modified
```

Browser already has the latest version.

---

# 4xx Client Errors

The problem is on the client side.

---

## 400 Bad Request

Invalid request data.

```http
400 Bad Request
```

Example:

```json
{
  "age": "abc"
}
```

when integer expected.

---

## 401 Unauthorized

Authentication required.

```text
401 Unauthorized
```

Example:

```text
Missing JWT token
```

---

## 403 Forbidden

Authenticated but not allowed.

```text
403 Forbidden
```

Example:

```text
User lacks admin permission
```

---

## 404 Not Found

Most common error.

```text
404 Not Found
```

Example:

```text
/users/999
```

User doesn't exist.

---

## 405 Method Not Allowed

Wrong HTTP method used.

Example:

```text
POST endpoint called with GET
```

Response:

```text
405 Method Not Allowed
```

---

## 409 Conflict

Conflict with existing data.

Example:

```text
Email already exists
```

Response:

```text
409 Conflict
```

---

## 422 Unprocessable Entity

Very common in FastAPI.

Example:

```json
{
  "age": "abc"
}
```

Expected:

```python
age: int
```

Response:

```text
422 Unprocessable Entity
```

Validation failed.

---

## 429 Too Many Requests

Rate limit exceeded.

```text
429 Too Many Requests
```

Example:

```text
API limit exceeded
```

---

# 5xx Server Errors

The problem is on the server.

---

## 500 Internal Server Error

Most common server error.

```text
500 Internal Server Error
```

Example:

```python
x = 10 / 0
```

Application crashes.

---

## 501 Not Implemented

Feature not implemented.

```text
501 Not Implemented
```

---

## 502 Bad Gateway

Occurs with reverse proxies.

```text
502 Bad Gateway
```

Example:

```text
Nginx
  ↓
Backend Offline
```

---

## 503 Service Unavailable

Server temporarily unavailable.

```text
503 Service Unavailable
```

Reasons:

* Maintenance
* High traffic

---

## 504 Gateway Timeout

Upstream service took too long.

```text
504 Gateway Timeout
```

Example:

```text
API waiting for database
```

---

# Common Status Codes in FastAPI

```python
from fastapi import FastAPI, status

app = FastAPI()

@app.post(
    "/users",
    status_code=status.HTTP_201_CREATED
)
def create_user():
    return {"message": "Created"}
```

---

# FastAPI Status Constants

```python
from fastapi import status
```

Examples:

```python
status.HTTP_200_OK
status.HTTP_201_CREATED
status.HTTP_204_NO_CONTENT
status.HTTP_400_BAD_REQUEST
status.HTTP_401_UNAUTHORIZED
status.HTTP_403_FORBIDDEN
status.HTTP_404_NOT_FOUND
status.HTTP_422_UNPROCESSABLE_ENTITY
status.HTTP_500_INTERNAL_SERVER_ERROR
```

---

# Practical API Examples

## GET User

```http
GET /users/1
```

Response:

```http
200 OK
```

---

## Create User

```http
POST /users
```

Response:

```http
201 Created
```

---

## Delete User

```http
DELETE /users/1
```

Response:

```http
204 No Content
```

---

## Invalid Request

```http
POST /users
```

Invalid data:

```json
{
  "age": "abc"
}
```

Response:

```http
422 Unprocessable Entity
```

---

## User Not Found

```http
GET /users/999
```

Response:

```http
404 Not Found
```

---

# Most Important Status Codes for Interviews

| Code | Meaning               |
| ---- | --------------------- |
| 200  | OK                    |
| 201  | Created               |
| 204  | No Content            |
| 301  | Moved Permanently     |
| 302  | Found                 |
| 400  | Bad Request           |
| 401  | Unauthorized          |
| 403  | Forbidden             |
| 404  | Not Found             |
| 405  | Method Not Allowed    |
| 409  | Conflict              |
| 422  | Unprocessable Entity  |
| 429  | Too Many Requests     |
| 500  | Internal Server Error |
| 502  | Bad Gateway           |
| 503  | Service Unavailable   |
| 504  | Gateway Timeout       |

---

# Quick Memory Trick

```text
1xx → Information
2xx → Success
3xx → Redirect
4xx → Client Error
5xx → Server Error
```

Popular Codes:

```text
200 → Success
201 → Created
404 → Not Found
401 → Unauthorized
403 → Forbidden
500 → Server Error
```

---

# Common Interview Questions

## What is HTTP 200?

Request processed successfully.

---

## Difference Between 401 and 403?

```text
401 → Not Authenticated
403 → Authenticated but Not Allowed
```

---

## Difference Between 200 and 201?

```text
200 → Existing resource returned
201 → New resource created
```

---

## Why Does FastAPI Return 422?

Because request validation failed.

---

## Difference Between 404 and 500?

```text
404 → Resource doesn't exist
500 → Server crashed or failed
```

---

# Interview Definition

HTTP Status Codes are standardized three-digit response codes returned by web servers to indicate the result of a client's request. They are categorized into informational, success, redirection, client error, and server error responses.
