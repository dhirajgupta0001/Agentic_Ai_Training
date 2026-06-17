# Agentic AI Training

This repository documents my daily coding practice, Data Structures & Algorithms (DSA) journey, and programming concepts learning using Java, Python, and AI Engineering tools.

## Progress

### Day 1

| Problem         | Approach                     | Language |
| --------------- | ---------------------------- | -------- |
| Two Sum         | Brute Force                  | Java     |
| Two Sum         | HashMap (Optimized)          | Java     |
| Add Two Numbers | Linked List + Carry Handling | Java     |

### Day 2

| Problem / Topic                                | Approach                    | Language |
| ---------------------------------------------- | --------------------------- | -------- |
| Longest Substring Without Repeating Characters | Sliding Window + HashSet    | Java     |
| Roman to Integer                               | HashMap + String Traversal  | Java     |
| Python Exceptions                              | Exception Handling Concepts | Python   |

### Day 3

| Problem / Topic                 | Approach                                 | Language |
| ------------------------------- | ---------------------------------------- | -------- |
| Longest Palindromic Substring   | Expand Around Center                     | Java     |
| Python Control Flow and Imports | Control Flow Statements & Module Imports | Python   |

### Day 4

| Problem / Topic                        | Approach             | Language |
| -------------------------------------- | -------------------- | -------- |
| Container With Most Water              | Two Pointers         | Java     |
| Longest Common Prefix                  | Horizontal Scanning  | Java     |
| Synchronous & Asynchronous Programming | Programming Concepts | Python   |

### Day 5

| Practice / Topic   | Concepts Covered                          | Language |
| ------------------ | ----------------------------------------- | -------- |
| Asyncio Practice 1 | create_task(), Event Loop Execution Order | Python   |
| Asyncio Practice 2 | Task Scheduling and Awaiting Tasks        | Python   |
| Asyncio Practice 3 | asyncio.gather() Concurrent Execution     | Python   |
| Asyncio Practice 4 | Sequential Await Execution                | Python   |
| Asyncio Practice 5 | Task Cancellation and CancelledError      | Python   |
| Asyncio Practice 6 | Exception Propagation in gather()         | Python   |
| Asyncio Practice 7 | return_exceptions=True in gather()        | Python   |

### Day 6

| Problem / Topic                   | Approach               | Language |
| --------------------------------- | ---------------------- | -------- |
| Rotting Oranges                   | Multi-Source BFS       | Java     |
| Simple LangChain Agent            | Agent + LLM Workflow   | Python   |
| Python 2 vs Python 3              | Version Comparison     | Python   |
| Python Virtual Environment (venv) | Environment Management | Python   |

### Day 7

| Problem / Topic       | Approach                    | Language |
| --------------------- | --------------------------- | -------- |
| Valid Parentheses     | Stack (LIFO)                | Java     |
| LangChain Chat Models | Chat Model Fundamentals     | Python   |
| init_chat_model()     | Model Initialization        | Python   |
| Python Classes        | Object-Oriented Programming | Python   |
| Shallow Copy          | Object Copying              | Python   |
| Deep Copy             | Memory Management           | Python   |
| UV Package Manager    | Modern Python Tooling       | Python   |

---

## Repository Structure

```text
Agentic_Ai_Training/
├── README.md
│
├── Day 1/
│   ├── README.md
│   ├── TwoSum.java
│   ├── TwoSum2.java
│   └── AddTwoNumbers.java
│
├── Day 2/
│   ├── README.md
│   ├── LengthOfLongestSubstring.java
│   ├── RomanToInteger.java
│   └── python_exceptions.md
│
├── Day 3/
│   ├── README.md
│   ├── LongestPalindromicSubstring.java
│   └── python_control_flow_and_imports.md
│
├── Day 4/
│   ├── README.md
│   ├── ContainerWithMostWater.java
│   ├── LongestCommonPrefix.java
│   └── synchronous_and_asynchronous_programming.md
│
├── Day 5/
│   ├── README.md
│   ├── Question1.py
│   ├── Question2.py
│   ├── Question3.py
│   ├── Question4.py
│   ├── Question5.py
│   ├── Question6.py
│   ├── Question7.py
│   └── tempCodeRunner.py
│
├── Day 6/
│   ├── README.md
│   ├── RottingOranges.java
│   ├── agent_demo.py
│   ├── python2_vs_python3.md
│   ├── python_venv_guide.md
│   ├── pyvenv.cfg
│   ├── tempCodeRunnerFile.py
│   └── langchain_guide.md
│
└── Day 7/
    ├── README.md
    ├── myproject
    ├── ChatOllama.py
    ├── langchain_chat_models_and_init_chat_model.md
    ├── ValidParentheses.java
    ├── python_classes.md
    ├── python_shallow_copy_deep_copy.md
    └── uv_python_package_manager_guide.md
```

---

## Topics Covered

### Data Structures & Algorithms

* Arrays
* HashMap
* HashSet
* Linked Lists
* Stack
* Queue
* Breadth-First Search (BFS)
* Multi-Source BFS
* Matrix Traversal
* Two Pointers
* Sliding Window
* Strings
* String Manipulation
* Prefix Matching
* Palindrome Detection
* Expand Around Center
* Horizontal Scanning
* Greedy Thinking
* Brute Force vs Optimized Solutions
* Time & Space Complexity Analysis

### Python

* Exception Handling
* Control Flow
* Module Imports
* Python 2 vs Python 3
* Virtual Environments (venv)
* UV Package Manager
* Dependency Management
* Classes and Objects
* Constructors (`__init__`)
* Shallow Copy
* Deep Copy
* Memory References
* Synchronous Programming
* Asynchronous Programming
* Event Loop
* Coroutines
* async / await
* create_task()
* asyncio.gather()
* Task Scheduling
* Concurrent Execution
* Sequential Execution
* Task Cancellation
* CancelledError
* Exception Handling in Async Programs
* return_exceptions=True

### AI Engineering

* LangChain Fundamentals
* LangChain Chat Models
* init_chat_model()
* AI Agents
* LLM Workflows
* Prompt Engineering Basics
* Tool Calling Concepts
* Agent Execution Flow

---

## Current Stats

| Day   | Problems / Topics Completed |
| ----- | --------------------------- |
| Day 1 | 3                           |
| Day 2 | 3                           |
| Day 3 | 2                           |
| Day 4 | 3                           |
| Day 5 | 7                           |
| Day 6 | 4                           |
| Day 7 | 7                           |
| Total | 29                          |

### Overall Progress

| Category                   | Count |
| -------------------------- | ----- |
| DSA Problems Solved        | 9     |
| Python Topics Learned      | 10    |
| Asyncio Practice Programs  | 7     |
| AI Projects / Agents Built | 1     |
| LangChain Topics Studied   | 3     |
| Total Learning Items       | 30    |

---

## Key Learnings

### Day 5

* Learned how Python's event loop schedules coroutines.
* Understood the difference between `await` and `create_task()`.
* Practiced running tasks concurrently using `asyncio.gather()`.
* Compared concurrent execution with sequential execution.
* Learned how task cancellation works using `task.cancel()`.
* Understood how `CancelledError` propagates through async code.
* Explored exception handling in asynchronous programs.
* Learned how `return_exceptions=True` prevents gather() from failing fast.

### Day 6

* Learned how Multi-Source BFS solves matrix traversal problems efficiently.
* Practiced queue-based graph traversal through the Rotting Oranges problem.
* Built a simple AI agent using LangChain.
* Studied Python 2 vs Python 3 differences.
* Practiced environment management using venv.

### Day 7

* Learned how stacks solve matching bracket problems efficiently.
* Practiced the LIFO principle through the Valid Parentheses problem.
* Studied LangChain chat models and `init_chat_model()`.
* Strengthened Python OOP fundamentals through classes.
* Understood shallow copy vs deep copy.
* Explored memory references and object duplication.
* Learned modern Python package management using UV.

---

## Author

**Dhiraj Gupta**

Learning, building, and documenting my journey toward becoming a stronger software engineer through consistent coding practice, algorithmic problem solving, AI engineering, and continuous learning.

