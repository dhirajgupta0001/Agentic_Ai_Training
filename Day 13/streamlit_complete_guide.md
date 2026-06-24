# Streamlit Complete Guide

## Introduction

Streamlit is an open-source Python framework used to build interactive web applications, dashboards, data science projects, machine learning applications, and AI tools using only Python code.

With Streamlit, developers can create web applications without needing:

* HTML
* CSS
* JavaScript

Streamlit automatically converts Python code into a web interface.

---

# Why Streamlit?

Traditional web development requires:

```text
Frontend
│
├── HTML
├── CSS
└── JavaScript

Backend
│
└── Python
```

Using Streamlit:

```text
Python
  │
  ▼
Web Application
```

Everything is built using Python.

---

# Installation

Using pip:

```bash
pip install streamlit
```

Using uv:

```bash
uv add streamlit
```

Verify installation:

```bash
streamlit --version
```

---

# Your First Streamlit App

Create a file named `app.py`.

```python
import streamlit as st

st.title("My First Streamlit App")

st.write("Hello World!")
```

Run:

```bash
streamlit run app.py
```

Output:

```text
Local URL:
http://localhost:8501
```

Browser:

```text
My First Streamlit App

Hello World!
```

---

# Understanding the Import

```python
import streamlit as st
```

`st` is the Streamlit module alias.

All Streamlit functions are accessed through:

```python
st.function_name()
```

Examples:

```python
st.title()
st.write()
st.button()
st.text_input()
```

---

# Displaying Text

## Title

```python
st.title("Streamlit Tutorial")
```

Output:

```text
# Streamlit Tutorial
```

---

## Header

```python
st.header("User Dashboard")
```

---

## Subheader

```python
st.subheader("Statistics")
```

---

## Text

```python
st.text("Hello Streamlit")
```

---

## Write

```python
st.write("Hello Streamlit")
```

The most commonly used display function.

---

# User Input Components

## Text Input

```python
name = st.text_input(
    "Enter your name"
)

st.write(name)
```

---

## Number Input

```python
age = st.number_input(
    "Enter age"
)
```

---

## Text Area

```python
message = st.text_area(
    "Enter message"
)
```

---

## Password Input

```python
password = st.text_input(
    "Password",
    type="password"
)
```

---

# Buttons

```python
if st.button("Click Me"):
    st.write("Button Pressed")
```

---

# Checkbox

```python
agree = st.checkbox(
    "I Agree"
)

if agree:
    st.write("Accepted")
```

---

# Radio Buttons

```python
gender = st.radio(
    "Gender",
    ["Male", "Female"]
)
```

---

# Select Box

```python
city = st.selectbox(
    "Choose City",
    ["Delhi", "Mumbai", "Pune"]
)

st.write(city)
```

---

# Multi Select

```python
skills = st.multiselect(
    "Select Skills",
    [
        "Python",
        "Java",
        "JavaScript"
    ]
)
```

---

# Slider

```python
age = st.slider(
    "Select Age",
    0,
    100
)

st.write(age)
```

---

# Date Input

```python
date = st.date_input(
    "Choose Date"
)
```

---

# Time Input

```python
time = st.time_input(
    "Select Time"
)
```

---

# Working with Data

## Table

```python
import pandas as pd

df = pd.DataFrame({
    "Name": ["John", "Alice"],
    "Age": [25, 30]
})

st.table(df)
```

---

## Interactive DataFrame

```python
st.dataframe(df)
```

Provides sorting and scrolling.

---

# Displaying JSON

```python
st.json({
    "name": "John",
    "age": 25
})
```

---

# Charts

## Line Chart

```python
import pandas as pd
import numpy as np

data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=["A", "B", "C"]
)

st.line_chart(data)
```

---

## Bar Chart

```python
st.bar_chart(data)
```

---

## Area Chart

```python
st.area_chart(data)
```

---

# Images

```python
st.image(
    "image.png",
    caption="Sample Image"
)
```

---

# Videos

```python
st.video("video.mp4")
```

---

# Audio

```python
st.audio("audio.mp3")
```

---

# File Upload

```python
uploaded_file = st.file_uploader(
    "Upload File"
)

if uploaded_file:
    st.write(
        uploaded_file.name
    )
```

---

# Sidebar

```python
st.sidebar.title("Menu")

option = st.sidebar.selectbox(
    "Choose",
    ["Home", "About"]
)
```

Layout:

```text
Sidebar
 ├─ Home
 └─ About
```

---

# Columns

```python
col1, col2 = st.columns(2)

with col1:
    st.write("Column 1")

with col2:
    st.write("Column 2")
```

---

# Containers

```python
container = st.container()

with container:
    st.write("Inside Container")
```

---

# Expander

```python
with st.expander(
    "More Details"
):
    st.write(
        "Hidden Content"
    )
```

---

# Session State

Session state stores data between reruns.

```python
if "count" not in st.session_state:
    st.session_state.count = 0

if st.button("Increment"):
    st.session_state.count += 1

st.write(
    st.session_state.count
)
```

---

# Caching

Useful for expensive operations.

```python
@st.cache_data
def load_data():
    return expensive_function()
```

Benefits:

* Faster performance
* Reduced API calls

---

# Streamlit Forms

```python
with st.form("my_form"):

    name = st.text_input(
        "Name"
    )

    submitted = st.form_submit_button(
        "Submit"
    )

    if submitted:
        st.write(name)
```

---

# Streamlit + Machine Learning

```python
prediction = model.predict(
    [[age]]
)

st.write(prediction)
```

Users can enter values and get predictions instantly.

---

# Streamlit + OpenAI

```python
import streamlit as st
from openai import OpenAI

client = OpenAI()

question = st.text_input(
    "Ask AI"
)

if question:

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": question
            }
        ]
    )

    st.write(
        response.choices[0]
        .message.content
    )
```

---

# Streamlit + LangChain

```python
from langchain_openai import ChatOpenAI
import streamlit as st

llm = ChatOpenAI()

question = st.text_input(
    "Ask Question"
)

if question:

    response = llm.invoke(
        question
    )

    st.write(
        response.content
    )
```

---

# Typical Project Structure

```text
streamlit_project/
│
├── app.py
├── requirements.txt
├── data.csv
├── model.pkl
├── .env
└── assets/
```

---

# Streamlit vs FastAPI

| Feature           | Streamlit       | FastAPI   |
| ----------------- | --------------- | --------- |
| Purpose           | UI Applications | APIs      |
| Frontend Included | Yes             | No        |
| Dashboards        | Excellent       | No        |
| API Creation      | Limited         | Excellent |
| ML Applications   | Excellent       | Good      |
| Learning Curve    | Easy            | Moderate  |

---

# When to Use Streamlit

Use Streamlit for:

* Data Science Projects
* Machine Learning Demos
* AI Chatbots
* Internal Tools
* Analytics Dashboards
* Data Visualization
* LLM Applications

---

# Advantages of Streamlit

* Easy to learn
* Pure Python
* Fast development
* Great for AI projects
* Built-in widgets
* Interactive dashboards

---

# Disadvantages of Streamlit

* Limited frontend customization
* Not ideal for large-scale production apps
* Less flexible than React + FastAPI

---

# Common Interview Questions

## What is Streamlit?

Streamlit is an open-source Python framework used to build interactive web applications using only Python code.

---

## Why is Streamlit Popular?

Because developers can create web applications without HTML, CSS, or JavaScript.

---

## How Do You Run a Streamlit App?

```bash
streamlit run app.py
```

---

## What Port Does Streamlit Use?

Default:

```text
8501
```

---

## Difference Between Streamlit and FastAPI?

```text
Streamlit → UI Applications

FastAPI → APIs
```

---

## What is Session State?

A mechanism for storing values across Streamlit reruns.

---

## What is Caching?

A way to store expensive computation results and improve performance.

---

# Best Practices

1. Use session state for user interactions.
2. Cache expensive operations.
3. Organize code into functions.
4. Store secrets in `.env` files.
5. Keep UI and business logic separate.

---

# Interview Definition

Streamlit is an open-source Python framework that enables developers to quickly build interactive web applications, dashboards, machine learning tools, and AI-powered applications using only Python code without requiring frontend technologies such as HTML, CSS, or JavaScript.
