## Problems Solved

### 1. Valid Parentheses

**File:** `ValidParentheses.java`

#### Problem Statement

Given a string containing only brackets:

```text
() {} []
```

Determine whether the input string is valid.

#### Approach

* Used a **Stack** to track opening brackets.
* Pushed opening brackets onto the stack.
* For every closing bracket:

  * Checked if the stack was empty.
  * Verified that the top element matched.
* Ensured the stack was empty at the end.

#### Concepts Used

* Stack
* LIFO Principle
* String Traversal
* Matching Pairs

#### Time Complexity

* **O(n)**

#### Space Complexity

* **O(n)**

---

## LangChain Learning

### 2. Chat Models & init_chat_model()

**File:** `langchain_chat_models.md`

#### Topics Covered

##### Chat Models

* Understanding chat-based LLMs
* User, System, and AI Messages
* Model invocation flow
* Message-based interactions

##### init_chat_model()

* Initializing chat models using LangChain
* Provider configuration
* Model selection
* API key integration

#### Concepts Learned

* Chat Model Architecture
* Message-Based Communication
* LangChain Model Initialization
* LLM Configuration

#### Example

```python
from langchain.chat_models import init_chat_model

model = init_chat_model(
    "gpt-4o-mini",
    model_provider="openai"
)
```

---

## Python Learning

### 3. Python Classes

**File:** `python_classes.md`

#### Topics Covered

* Classes and Objects
* Constructors (`__init__`)
* Instance Variables
* Methods
* Object Creation
* Encapsulation Basics

#### Example

```python
class Student:
    def __init__(self, name):
        self.name = name

    def display(self):
        print(self.name)
```

#### Learning Outcome

* Understood object-oriented programming fundamentals.
* Learned how classes help organize code.

---

### 4. Shallow Copy vs Deep Copy

**File:** `python_copying.md`

#### Topics Covered

##### Shallow Copy

* Copies only the outer object.
* Nested objects are shared.

##### Deep Copy

* Creates completely independent copies.
* Nested objects are also copied.

#### Example

```python
import copy

original = [[1, 2], [3, 4]]

shallow = copy.copy(original)
deep = copy.deepcopy(original)
```

#### Learning Outcome

* Learned memory reference behavior.
* Understood when to use shallow copy vs deep copy.

---

### 5. UV Package Manager

**File:** `python_uv.md`

#### Topics Covered

* What is UV?
* Faster Python package management
* Virtual environment creation
* Dependency installation
* Project management

#### Commands Practiced

Install UV:

```bash
pip install uv
```

Create Environment:

```bash
uv venv
```

Install Package:

```bash
uv pip install langchain
```

#### Learning Outcome

* Learned modern Python package management.
* Explored faster alternatives to pip and venv.

---

## Repository Structure

```text
Day 7/
├── README.md
├── ValidParentheses.java
├── langchain_chat_models.md
├── python_classes.md
├── python_copying.md
└── python_uv.md
```

---

## Key Learnings

### DSA

* Learned how stacks solve bracket matching problems.
* Practiced LIFO-based problem solving.
* Improved understanding of stack applications.

### LangChain

* Learned how chat models work.
* Understood model initialization using `init_chat_model()`.
* Explored message-based interactions in LangChain.

### Python

* Learned object-oriented programming basics using classes.
* Understood the difference between shallow and deep copies.
* Explored memory references and object duplication.
* Learned how UV simplifies Python dependency management.

---

## Progress Summary

✅ Valid Parentheses

✅ LangChain Chat Models

✅ init_chat_model()

✅ Python Classes

✅ Shallow Copy

✅ Deep Copy

✅ UV Package Manager

---

## Reflection

Day 7 combined algorithmic problem solving with AI engineering and Python fundamentals. Alongside strengthening stack concepts through the Valid Parentheses problem, I gained a deeper understanding of LangChain chat models, object-oriented programming in Python, memory management through copying techniques, and modern Python tooling with UV.
