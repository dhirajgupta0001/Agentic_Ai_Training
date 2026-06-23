# Cookies Complete Guide

## Introduction

Cookies are small pieces of data stored by a web browser and automatically sent back to the server with future requests.

Cookies help websites remember information about users across multiple requests.

Common uses:

* Authentication
* Session management
* User preferences
* Shopping carts
* Analytics and tracking

---

# What is a Cookie?

When a user visits a website:

```text
Browser
   │
Request
   ▼
Server
```

The server can send:

```http
Set-Cookie: session_id=abc123
```

The browser stores this cookie.

Future requests automatically include:

```http
Cookie: session_id=abc123
```

The server can then identify the user.

---

# Why Cookies Are Needed

HTTP is stateless.

This means:

```text
Request 1
Server responds

Request 2
Server does not remember Request 1
```

Without cookies:

```text
User Logs In
      ↓
Server Authenticates
      ↓
Next Request
      ↓
Server Doesn't Know User
```

With cookies:

```text
User Logs In
      ↓
Cookie Created
      ↓
Browser Stores Cookie
      ↓
Future Requests Include Cookie
      ↓
Server Recognizes User
```

---

# Cookie Lifecycle

```text
Client
   │
Login Request
   ▼
Server
   │
Set-Cookie
   ▼
Browser Stores Cookie
   │
Future Requests
   ▼
Cookie Sent Automatically
```

---

# Example HTTP Response

Server response:

```http
HTTP/1.1 200 OK

Set-Cookie: session_id=abc123
```

Browser stores:

```text
session_id=abc123
```

---

# Future Request Example

```http
GET /profile HTTP/1.1

Cookie: session_id=abc123
```

Server reads the cookie and identifies the user.

---

# Cookie Structure

Example:

```http
Set-Cookie:
session_id=abc123;
Path=/;
HttpOnly;
Secure;
Max-Age=3600
```

---

# Cookie Attributes

| Attribute | Purpose                       |
| --------- | ----------------------------- |
| Name      | Cookie identifier             |
| Value     | Stored value                  |
| Path      | URL scope                     |
| Domain    | Website scope                 |
| Secure    | HTTPS only                    |
| HttpOnly  | Not accessible via JavaScript |
| Max-Age   | Expiration time               |
| SameSite  | CSRF protection               |

---

# Creating Cookies in FastAPI

Example:

```python
from fastapi import FastAPI, Response

app = FastAPI()

@app.get("/login")
def login(response: Response):

    response.set_cookie(
        key="username",
        value="john"
    )

    return {
        "message": "Logged In"
    }
```

Response:

```http
Set-Cookie: username=john
```

---

# Reading Cookies in FastAPI

```python
from fastapi import Cookie

@app.get("/profile")
def profile(
    username: str = Cookie(None)
):
    return {
        "username": username
    }
```

Request:

```http
Cookie: username=john
```

Response:

```json
{
    "username": "john"
}
```

---

# Deleting Cookies

```python
from fastapi import Response

@app.get("/logout")
def logout(response: Response):

    response.delete_cookie(
        key="username"
    )

    return {
        "message": "Logged Out"
    }
```

---

# Session Cookies

Session cookies exist only while the browser remains open.

Example:

```http
Set-Cookie: session_id=abc123
```

When browser closes:

```text
Cookie removed
```

Use cases:

* Login sessions
* Temporary authentication

---

# Persistent Cookies

Persistent cookies remain after browser restarts.

Example:

```http
Set-Cookie:
theme=dark;
Max-Age=86400
```

Stored for:

```text
24 Hours
```

Use cases:

* Remember Me
* Theme preferences
* Language settings

---

# Types of Cookies

## Session Cookies

```text
Temporary
Deleted when browser closes
```

---

## Persistent Cookies

```text
Stored on disk
Remain after restart
```

---

## Secure Cookies

Only sent through HTTPS.

```http
Set-Cookie:
session=abc123;
Secure
```

---

## HttpOnly Cookies

JavaScript cannot access them.

```http
Set-Cookie:
session=abc123;
HttpOnly
```

Protection against:

```javascript
document.cookie
```

attacks.

---

## SameSite Cookies

Protect against Cross-Site Request Forgery (CSRF).

```http
Set-Cookie:
session=abc123;
SameSite=Strict
```

Available values:

```text
Strict
Lax
None
```

---

# Cookies vs Sessions

Developers often confuse these.

### Cookie

Stored on:

```text
Browser
```

Example:

```text
session_id=abc123
```

---

### Session

Stored on:

```text
Server
```

Example:

```text
abc123 → User ID 42
```

---

# Authentication Flow

```text
User Login
      │
      ▼
Server Creates Session
      │
      ▼
Session ID Generated
      │
      ▼
Cookie Sent
      │
      ▼
Browser Stores Cookie
      │
      ▼
Future Requests
      │
Cookie Sent
      ▼
Server Finds Session
```

---

# Cookies vs Local Storage

| Feature                   | Cookies   | Local Storage |
| ------------------------- | --------- | ------------- |
| Sent to Server            | Yes       | No            |
| Storage Size              | ~4KB      | ~5MB          |
| Expiration                | Supported | Manual        |
| Auto Included in Requests | Yes       | No            |
| Authentication Usage      | Common    | Less Secure   |

---

# Working with Cookies in JavaScript

## Create Cookie

```javascript
document.cookie =
"user=John";
```

---

## Read Cookie

```javascript
console.log(
    document.cookie
);
```

---

## Delete Cookie

```javascript
document.cookie =
"user=; expires=Thu, 01 Jan 1970 00:00:00 UTC";
```

---

# Security Risks

## XSS (Cross-Site Scripting)

Malicious script:

```javascript
alert(document.cookie)
```

Protection:

```http
HttpOnly
```

---

## CSRF (Cross-Site Request Forgery)

Protection:

```http
SameSite=Strict
```

---

# Secure Authentication Cookie Example

```http
Set-Cookie:
session_id=abc123;
HttpOnly;
Secure;
SameSite=Strict
```

Recommended for login systems.

---

# Cookies in React

Login request:

```javascript
fetch("/login", {
  method: "POST",
  credentials: "include"
});
```

Important:

```javascript
credentials: "include"
```

Allows browser cookies to be sent with requests.

---

# FastAPI Cookie Authentication Example

```python
from fastapi import FastAPI, Response

app = FastAPI()

@app.post("/login")
def login(response: Response):

    response.set_cookie(
        key="session",
        value="abc123",
        httponly=True
    )

    return {
        "message": "Logged In"
    }
```

Protected route:

```python
from fastapi import Cookie

@app.get("/profile")
def profile(
    session: str = Cookie(None)
):
    return {
        "session": session
    }
```

---

# Advantages of Cookies

* Automatic transmission with requests
* Session management
* User authentication
* Preference storage
* Widely supported

---

# Disadvantages of Cookies

* Small storage size
* Sent with every request
* Privacy concerns
* Security risks if misconfigured

---

# Common Interview Questions

## What is a Cookie?

A small piece of data stored in the browser and sent automatically with future requests.

---

## Where Are Cookies Stored?

```text
Browser
```

---

## Difference Between Cookies and Sessions?

```text
Cookie  → Browser
Session → Server
```

---

## What Does HttpOnly Do?

Prevents JavaScript from reading the cookie.

---

## What Does Secure Do?

Ensures the cookie is sent only over HTTPS.

---

## What Does SameSite Protect Against?

Cross-Site Request Forgery (CSRF) attacks.

---

## Cookies vs Local Storage?

| Cookies             | Local Storage               |
| ------------------- | --------------------------- |
| Sent automatically  | Not sent automatically      |
| Smaller storage     | Larger storage              |
| Better for sessions | Better for client-side data |

---

# Best Practices

1. Use `HttpOnly` for authentication cookies.
2. Use `Secure` in production.
3. Use `SameSite=Strict` when possible.
4. Avoid storing sensitive data directly in cookies.
5. Use short expiration times for session cookies.

---

# Interview Definition

Cookies are small pieces of data stored in a user's browser and automatically sent with future requests to the same server. They are commonly used for authentication, session management, personalization, and tracking user activity.
