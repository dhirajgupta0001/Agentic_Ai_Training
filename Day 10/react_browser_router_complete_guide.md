# BrowserRouter in React.js Complete Guide

## Introduction

BrowserRouter is a component provided by React Router that enables client-side routing in React applications.

It allows users to navigate between pages without reloading the entire browser window, making React applications behave like Single Page Applications (SPAs).

BrowserRouter uses the browser's History API to keep the UI synchronized with the URL.

---

# What Problem Does BrowserRouter Solve?

Traditional websites work like this:

```text
User Clicks Link
        ↓
Browser Sends Request
        ↓
Server Returns New HTML Page
        ↓
Entire Page Reloads
```

This process is slower because the browser reloads everything.

React applications use BrowserRouter:

```text
User Clicks Link
        ↓
React Router Handles Navigation
        ↓
URL Changes
        ↓
Component Changes
        ↓
No Page Reload
```

Only the required component updates.

---

# What is Client-Side Routing?

Client-side routing means navigation happens inside the browser without requesting a new HTML page from the server.

Example URLs:

```text
/
/about
/contact
/products
```

Instead of loading a new page, React renders different components based on the URL.

---

# Installing React Router

Install React Router:

```bash
npm install react-router-dom
```

or

```bash
yarn add react-router-dom
```

---

# Setting Up BrowserRouter

## main.jsx

```jsx
import React from "react";
import ReactDOM from "react-dom/client";
import App from "./App";
import { BrowserRouter } from "react-router-dom";

ReactDOM.createRoot(
  document.getElementById("root")
).render(
  <BrowserRouter>
    <App />
  </BrowserRouter>
);
```

BrowserRouter wraps the entire application and enables routing.

---

# Creating Routes

## App.jsx

```jsx
import {
  Routes,
  Route
} from "react-router-dom";

function Home() {
  return <h1>Home Page</h1>;
}

function About() {
  return <h1>About Page</h1>;
}

function Contact() {
  return <h1>Contact Page</h1>;
}

function App() {
  return (
    <Routes>
      <Route
        path="/"
        element={<Home />}
      />

      <Route
        path="/about"
        element={<About />}
      />

      <Route
        path="/contact"
        element={<Contact />}
      />
    </Routes>
  );
}

export default App;
```

---

# Understanding Routes

```jsx
<Route
  path="/about"
  element={<About />}
/>
```

Explanation:

```text
path     → URL
element  → Component to render
```

When URL becomes:

```text
/about
```

React renders:

```jsx
<About />
```

---

# Navigation Using Link

Avoid using:

```html
<a href="/about">About</a>
```

because it reloads the page.

Instead use:

```jsx
import { Link } from "react-router-dom";

<Link to="/about">
  About
</Link>
```

Benefits:

* No page refresh
* Faster navigation
* Better user experience

---

# Example Navigation Bar

```jsx
import { Link } from "react-router-dom";

function Navbar() {
  return (
    <nav>
      <Link to="/">Home</Link>

      <Link to="/about">
        About
      </Link>

      <Link to="/contact">
        Contact
      </Link>
    </nav>
  );
}
```

---

# BrowserRouter and History API

BrowserRouter uses:

```javascript
window.history
```

Important methods:

```javascript
history.pushState()
history.replaceState()
```

These methods update the URL without reloading the page.

---

# Route Matching Process

```text
Current URL
      ↓
BrowserRouter
      ↓
Routes
      ↓
Matching Route
      ↓
Render Component
```

Example:

```text
/about
```

matches:

```jsx
<Route
  path="/about"
  element={<About />}
/>
```

and renders:

```jsx
<About />
```

---

# Dynamic Routes

Dynamic routes allow parameters inside URLs.

Example:

```jsx
<Route
  path="/users/:id"
  element={<User />}
/>
```

URLs:

```text
/users/1
/users/2
/users/10
```

---

# Accessing Route Parameters

Use:

```jsx
useParams()
```

Example:

```jsx
import { useParams }
from "react-router-dom";

function User() {

  const { id } =
    useParams();

  return (
    <h1>User {id}</h1>
  );
}
```

URL:

```text
/users/10
```

Output:

```text
User 10
```

---

# Nested Routes

Nested routes help organize larger applications.

Example:

```jsx
<Route
  path="/dashboard"
  element={<Dashboard />}
>
  <Route
    path="profile"
    element={<Profile />}
  />

  <Route
    path="settings"
    element={<Settings />}
  />
</Route>
```

Generated URLs:

```text
/dashboard/profile
/dashboard/settings
```

---

# Programmatic Navigation

Sometimes navigation happens through code.

Use:

```jsx
useNavigate()
```

Example:

```jsx
import {
  useNavigate
} from "react-router-dom";

function Login() {

  const navigate =
    useNavigate();

  const handleLogin = () => {
    navigate("/dashboard");
  };

  return (
    <button
      onClick={handleLogin}
    >
      Login
    </button>
  );
}
```

After login:

```text
/dashboard
```

opens automatically.

---

# BrowserRouter vs HashRouter

## BrowserRouter

URL:

```text
https://example.com/about
```

Uses History API.

---

## HashRouter

URL:

```text
https://example.com/#/about
```

Uses URL hash.

---

# Comparison

| Feature                | BrowserRouter | HashRouter  |
| ---------------------- | ------------- | ----------- |
| Clean URLs             | Yes           | No          |
| Uses History API       | Yes           | No          |
| SEO Friendly           | Better        | Limited     |
| Requires Server Config | Yes           | No          |
| Modern Applications    | Recommended   | Less Common |

---

# Common Project Structure

```text
src/
│
├── pages/
│   ├── Home.jsx
│   ├── About.jsx
│   ├── Contact.jsx
│
├── components/
│   └── Navbar.jsx
│
├── App.jsx
└── main.jsx
```

---

# Complete Example

## main.jsx

```jsx
import ReactDOM from "react-dom/client";
import {
  BrowserRouter
} from "react-router-dom";

import App from "./App";

ReactDOM.createRoot(
  document.getElementById("root")
).render(
  <BrowserRouter>
    <App />
  </BrowserRouter>
);
```

---

## App.jsx

```jsx
import {
  Routes,
  Route,
  Link
} from "react-router-dom";

function Home() {
  return <h1>Home</h1>;
}

function About() {
  return <h1>About</h1>;
}

export default function App() {

  return (
    <>
      <nav>
        <Link to="/">
          Home
        </Link>

        <Link to="/about">
          About
        </Link>
      </nav>

      <Routes>

        <Route
          path="/"
          element={<Home />}
        />

        <Route
          path="/about"
          element={<About />}
        />

      </Routes>
    </>
  );
}
```

---

# Advantages of BrowserRouter

* Clean URLs
* Faster navigation
* Better user experience
* Supports dynamic routes
* Supports nested routes
* Integrates with React Router
* Ideal for Single Page Applications

---

# Common Interview Questions

## What is BrowserRouter?

BrowserRouter is a React Router component that enables client-side routing using the browser's History API.

---

## Why do we use BrowserRouter?

To navigate between pages without reloading the browser.

---

## What API does BrowserRouter use?

```javascript
window.history
```

---

## Difference Between Link and Anchor Tag?

| Link           | Anchor Tag             |
| -------------- | ---------------------- |
| No page reload | Reloads page           |
| SPA navigation | Traditional navigation |
| Faster         | Slower                 |

---

## Difference Between BrowserRouter and HashRouter?

BrowserRouter creates clean URLs using the History API, while HashRouter uses URL fragments (#).

---

## What is useNavigate()?

A React Router hook used for programmatic navigation.

---

## What is useParams()?

A React Router hook used to access dynamic route parameters.

---

# Interview Definition

BrowserRouter is a React Router component that enables client-side routing by using the browser's History API. It allows React applications to update the URL and render different components without reloading the page, making Single Page Applications fast and responsive.
