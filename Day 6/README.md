## Problems Solved

### 1. Rotting Oranges

**File:** `RottingOranges.java`

#### Problem Statement

Given a grid where:

* `0` = Empty cell
* `1` = Fresh orange
* `2` = Rotten orange

Every minute, any fresh orange adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes required to rot all oranges, or `-1` if impossible.

#### Approach

* Used **Multi-Source Breadth-First Search (BFS)**.
* Added all rotten oranges to a queue initially.
* Processed oranges level by level.
* Each BFS level represented one minute.
* Tracked remaining fresh oranges.

#### Concepts Used

* Graph Traversal
* Breadth-First Search (BFS)
* Multi-Source BFS
* Queue Data Structure
* Matrix Traversal

#### Time Complexity

* **O(m × n)**

#### Space Complexity

* **O(m × n)**

---

## AI Engineering

### 2. Simple LangChain Agent

**File:** `simple_langchain_agent.py`

#### Objective

Created a basic AI agent using LangChain to understand how agents interact with language models and tools.

#### Concepts Learned

* LangChain Fundamentals
* Agents
* Prompts
* LLM Integration
* Tool Usage
* Agent Execution Flow

#### Key Takeaways

* Agents can decide which actions to perform.
* Tools extend the capabilities of language models.
* LangChain simplifies building AI-powered workflows.
* Understanding agents is foundational for Agentic AI development.

---

## Python Learning

### 3. Python 2 vs Python 3

**File:** `python2_vs_python3.md`

#### Topics Covered

##### Python 2

* Legacy version
* End-of-life support
* Older syntax

##### Python 3

* Current and actively maintained version
* Improved Unicode support
* Better syntax and features
* Enhanced performance and security

#### Key Differences

| Feature  | Python 2                    | Python 3                 |
| -------- | --------------------------- | ------------------------ |
| print    | print "Hello"               | print("Hello")           |
| Division | Integer division by default | True division            |
| Unicode  | Limited support             | Built-in Unicode support |
| Support  | Ended                       | Active                   |

#### Learning Outcome

* Understood why Python 3 is the industry standard.
* Learned migration benefits from Python 2 to Python 3.

---

### 4. Python Virtual Environments (venv)

**File:** `python_venv.md`

#### Topics Covered

##### What is a Virtual Environment?

A virtual environment is an isolated Python environment that allows projects to manage dependencies independently.

##### Commands Practiced

Create environment:

```bash id="3q0h61"
python -m venv venv
```

Activate (Windows):

```bash id="9hck4u"
venv\Scripts\activate
```

Activate (Linux/Mac):

```bash id="wjlwmv"
source venv/bin/activate
```

Deactivate:

```bash id="w24ic6"
deactivate
```

#### Learning Outcome

* Understood dependency isolation.
* Learned project-specific package management.
* Practiced creating and activating virtual environments.

---

## Key Learnings

### DSA

* Learned how Multi-Source BFS works.
* Understood level-order traversal in matrix problems.
* Practiced queue-based graph traversal.

### AI Engineering

* Built a simple LangChain agent.
* Understood the role of agents and tools.
* Learned foundational concepts of Agentic AI systems.

### Python

* Compared Python 2 and Python 3.
* Learned why Python 3 is preferred in modern development.
* Practiced working with virtual environments using venv.
* Improved environment and dependency management skills.

---

## Progress Summary

✅ Rotting Oranges

✅ Simple LangChain Agent

✅ Python 2 vs Python 3

✅ Python Virtual Environments (venv)

---

## Reflection

Day 6 expanded beyond algorithmic problem-solving into AI engineering and Python ecosystem fundamentals. Alongside practicing BFS through the Rotting Oranges problem, I gained hands-on experience with LangChain agents and strengthened my understanding of Python environments and version differences, which are essential skills for modern AI and software development.
