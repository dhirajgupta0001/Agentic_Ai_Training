## Problems Solved

### 1. Merge Two Sorted Lists

**File:** `MergeTwoSortedLists.java`

#### Problem Statement

Merge two sorted linked lists and return the merged sorted list.

#### Approach

* Used a **Dummy Node** to simplify list construction.
* Compared nodes from both linked lists.
* Added the smaller node to the result list.
* Attached remaining nodes after one list was exhausted.

#### Concepts Used

* Linked Lists
* Two Pointers
* Dummy Node Technique

#### Time Complexity

* **O(n + m)**

#### Space Complexity

* **O(1)**

#### Learning Outcome

* Strengthened Linked List manipulation skills.
* Learned how dummy nodes simplify linked list problems.

---

### 2. Letter Combinations of a Phone Number

**File:** `LetterCombinationsOfPhoneNumber.java`

#### Problem Statement

Given a string containing digits from 2–9, return all possible letter combinations that the number could represent.

#### Approach

* Used **Backtracking**.
* Mapped digits to corresponding characters.
* Generated combinations recursively.
* Applied the choose → explore → undo pattern.

#### Concepts Used

* Backtracking
* Recursion
* String Manipulation
* Decision Trees

#### Time Complexity

* **O(4ⁿ)**

#### Space Complexity

* **O(n)**

#### Learning Outcome

* Understood recursive problem solving.
* Practiced generating combinations using backtracking.

---

## AI Engineering

### 3. LangChain + Ollama + Llama 3.1

**File:** `langchain_ollama_llama3_examples.py`

#### Objective

Learned how to run local Large Language Models using Ollama and integrate them with LangChain.

#### Topics Covered

##### Ollama Fundamentals

* Installing Ollama
* Running local models
* Managing local LLMs

##### Llama 3.1

* Local inference
* Prompt execution
* Response generation

##### LangChain Integration

* ChatOllama
* Model initialization
* Prompt invocation
* Response handling

#### Example

```python
from langchain_ollama import ChatOllama

llm = ChatOllama(model="llama3.1")

response = llm.invoke("Explain Python in simple terms")

print(response.content)
```

#### Concepts Learned

* Local LLM execution
* LangChain model integration
* Prompt-response workflows
* AI application development

---

## Key Learnings

### DSA

* Practiced Linked List traversal and merging techniques.
* Learned how dummy nodes simplify pointer management.
* Strengthened understanding of recursion and backtracking.
* Explored tree-like decision making for generating combinations.

### AI Engineering

* Learned how to run Llama 3.1 locally using Ollama.
* Understood LangChain's ChatOllama integration.
* Practiced invoking local LLMs through LangChain.
* Gained hands-on experience with local AI workflows.

---

## Progress Summary

✅ Merge Two Sorted Lists

✅ Letter Combinations of a Phone Number

✅ LangChain Ollama Setup

✅ Llama 3.1 Examples

✅ ChatOllama Integration

---

## Reflection

Day 8 combined algorithmic problem-solving with practical AI engineering. Alongside strengthening Linked List and Backtracking concepts through LeetCode problems, I explored running local LLMs using Ollama and integrated Llama 3.1 with LangChain, gaining valuable experience in building AI-powered applications without relying on cloud-hosted models.
