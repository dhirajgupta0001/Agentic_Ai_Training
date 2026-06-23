# Local Storage and Session Storage Complete Guide

## Introduction

Local Storage and Session Storage are browser-based storage mechanisms provided by the Web Storage API.

They allow web applications to store data directly in the user's browser without sending it to the server automatically.

Common uses:

* User preferences
* Theme settings
* Shopping cart data
* Form progress
* Temporary application state

---

# What is Web Storage?

Web Storage provides two storage mechanisms:

1. Local Storage
2. Session Storage

```text
Browser
   │
   ├── Cookies
   │
   ├── Local Storage
   │
   └── Session Storage
```

Unlike cookies:

* Data is not automatically sent to the server
* Larger storage capacity
* Easier to use via JavaScript

---

# Why Do We Need Browser Storage?

Suppose a user chooses:

```text
Theme = Dark Mode
Language = English
```

Without storage:

```text
Refresh Page
    ↓
Preferences Lost
```

With storage:

```text
Save Preferences
    ↓
Refresh Page
    ↓
Preferences Restored
```

---

# Local Storage

Local Storage stores data permanently until it is manually removed.

Characteristics:

* Persistent storage
* Shared across browser tabs (same origin)
* Survives browser restarts
* Approximately 5–10 MB storage

---

# Storing Data in Local Storage

```javascript
localStorage.setItem(
    "username",
    "John"
);
```

---

# Retrieving Data

```javascript
const username =
    localStorage.getItem(
        "username"
    );

console.log(username);
```

Output:

```text
John
```

---

# Updating Data

```javascript
localStorage.setItem(
    "username",
    "Alice"
);
```

---

# Removing Data

```javascript
localStorage.removeItem(
    "username"
);
```

---

# Clearing Local Storage

```javascript
localStorage.clear();
```

Removes all stored values.

---

# Local Storage Lifecycle

```text
Save Data
    ↓
Close Browser
    ↓
Open Browser Again
    ↓
Data Still Exists
```

---

# Session Storage

Session Storage stores data only for the duration of the current browser tab session.

Characteristics:

* Temporary storage
* Tab-specific
* Removed when tab closes
* Approximately 5 MB storage

---

# Storing Data in Session Storage

```javascript
sessionStorage.setItem(
    "token",
    "abc123"
);
```

---

# Retrieving Data

```javascript
const token =
    sessionStorage.getItem(
        "token"
    );

console.log(token);
```

---

# Removing Data

```javascript
sessionStorage.removeItem(
    "token"
);
```

---

# Clearing Session Storage

```javascript
sessionStorage.clear();
```

---

# Session Storage Lifecycle

```text
Save Data
    ↓
Close Tab
    ↓
Open New Tab
    ↓
Data Gone
```

---

# Local Storage vs Session Storage

| Feature                   | Local Storage         | Session Storage |
| ------------------------- | --------------------- | --------------- |
| Storage Size              | ~5–10 MB              | ~5 MB           |
| Expiration                | Never (until deleted) | When tab closes |
| Shared Across Tabs        | Yes                   | No              |
| Browser Restart           | Data remains          | Data removed    |
| Sent to Server            | No                    | No              |
| Accessible via JavaScript | Yes                   | Yes             |

---

# Example: Theme Preference Using Local Storage

Save theme:

```javascript
localStorage.setItem(
    "theme",
    "dark"
);
```

Retrieve theme:

```javascript
const theme =
    localStorage.getItem(
        "theme"
    );

console.log(theme);
```

Output:

```text
dark
```

Even after restarting the browser, the value remains.

---

# Example: Temporary Form Data Using Session Storage

```javascript
sessionStorage.setItem(
    "step",
    "2"
);
```

Retrieve:

```javascript
const step =
    sessionStorage.getItem(
        "step"
    );
```

When the tab closes:

```text
step removed
```

---

# Storing Objects

Web Storage only stores strings.

---

## Incorrect Way

```javascript
const user = {
    name: "John",
    age: 25
};

localStorage.setItem(
    "user",
    user
);
```

Result:

```text
[object Object]
```

---

## Correct Way

Use JSON serialization.

```javascript
const user = {
    name: "John",
    age: 25
};

localStorage.setItem(
    "user",
    JSON.stringify(user)
);
```

---

## Reading Object Data

```javascript
const user =
    JSON.parse(
        localStorage.getItem(
            "user"
        )
    );

console.log(user.name);
```

Output:

```text
John
```

---

# React Example

Saving theme:

```jsx
localStorage.setItem(
    "theme",
    "dark"
);
```

Reading theme:

```jsx
const theme =
    localStorage.getItem(
        "theme"
    );
```

---

# React Component Example

```jsx
import { useState } from "react";

function App() {

    const [theme, setTheme] =
        useState(
            localStorage.getItem(
                "theme"
            ) || "light"
        );

    const changeTheme = () => {

        localStorage.setItem(
            "theme",
            "dark"
        );

        setTheme("dark");
    };

    return (
        <button
            onClick={changeTheme}
        >
            Dark Mode
        </button>
    );
}

export default App;
```

---

# Common Use Cases

## Local Storage

Store:

* Theme preference
* Language settings
* Sidebar state
* Recently viewed items
* Non-sensitive application settings

Example:

```text
Dark Mode
Language
User Preferences
```

---

## Session Storage

Store:

* Temporary form data
* Checkout progress
* Search filters
* Current tab state

Example:

```text
Current Checkout Step
Temporary Search Results
```

---

# Security Considerations

Both storage types are accessible through JavaScript:

```javascript
localStorage.getItem("token");
sessionStorage.getItem("token");
```

Because of this:

Do NOT store:

* Passwords
* API secrets
* Sensitive personal information

They can be exposed through XSS attacks.

---

# Local Storage vs Cookies

| Feature              | Local Storage | Cookies               |
| -------------------- | ------------- | --------------------- |
| Size                 | ~5 MB         | ~4 KB                 |
| Sent to Server       | No            | Yes                   |
| Expiration           | Manual        | Supported             |
| JavaScript Access    | Yes           | Yes (unless HttpOnly) |
| Authentication Usage | Less Secure   | Common                |

---

# Session Storage vs Cookies

| Feature            | Session Storage | Cookies |
| ------------------ | --------------- | ------- |
| Sent Automatically | No              | Yes     |
| Server Access      | No              | Yes     |
| Tab Specific       | Yes             | No      |
| Storage Size       | Larger          | Smaller |

---

# When to Use Which?

## Use Cookies

For:

* Authentication sessions
* Refresh tokens
* Server-side session tracking

---

## Use Local Storage

For:

* User preferences
* Theme settings
* Persistent non-sensitive data

---

## Use Session Storage

For:

* Temporary data
* Multi-step forms
* Checkout progress
* Per-tab application state

---

# Advantages of Local Storage

* Persistent storage
* Easy to use
* Large storage capacity
* Available across browser sessions

---

# Advantages of Session Storage

* Temporary storage
* Automatically cleaned up
* Ideal for tab-specific state

---

# Disadvantages

## Local Storage

* Accessible via JavaScript
* Vulnerable to XSS
* No automatic expiration

---

## Session Storage

* Data lost when tab closes
* Not shared across tabs

---

# Common Interview Questions

## What is Local Storage?

A browser storage mechanism that stores data permanently until explicitly removed.

---

## What is Session Storage?

A browser storage mechanism that stores data only for the lifetime of a browser tab.

---

## Difference Between Local Storage and Session Storage?

```text
Local Storage:
Persistent

Session Storage:
Temporary
Removed when tab closes
```

---

## Can They Store Objects?

Not directly.

Use:

```javascript
JSON.stringify()
JSON.parse()
```

---

## Are They Sent to the Server Automatically?

No.

Unlike cookies, neither Local Storage nor Session Storage is automatically included in HTTP requests.

---

## Which is Better for Authentication?

Generally:

```text
HttpOnly Cookies
```

are safer than:

```text
Local Storage
```

for storing authentication tokens.

---

# Best Practices

1. Store only non-sensitive data.
2. Use JSON serialization for objects.
3. Use Local Storage for persistent preferences.
4. Use Session Storage for temporary state.
5. Use HttpOnly cookies for authentication tokens.

---

# Interview Definition

Local Storage and Session Storage are browser-based storage mechanisms provided by the Web Storage API. Local Storage persists data until explicitly removed, while Session Storage stores data only for the lifetime of a browser tab or session.
