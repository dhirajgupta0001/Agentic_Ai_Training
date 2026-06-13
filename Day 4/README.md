

## Problems Solved

### 1. Container With Most Water

**File:** `ContainerWithMostWater.java`

#### Problem Statement

Given an array of heights, find two lines that together with the x-axis form a container that holds the maximum amount of water.

#### Approach

* Used the **Two Pointers** technique.
* Started with pointers at both ends of the array.
* Calculated the area formed by the two lines.
* Moved the pointer with the smaller height inward.
* Kept track of the maximum area found.

#### Concepts Used

* Arrays
* Two Pointers
* Greedy Thinking
* Optimization

#### Time Complexity

* **O(n)**

#### Space Complexity

* **O(1)**

#### Example

```text id="gg0jtp"
Input:  [1,8,6,2,5,4,8,3,7]
Output: 49
```

---

### 2. Longest Common Prefix

**File:** `LongestCommonPrefix.java`

#### Problem Statement

Find the longest common prefix string amongst an array of strings.

#### Approach

* Used **Horizontal Scanning**.
* Assumed the first string as the initial prefix.
* Compared it with each string.
* Reduced the prefix until a match was found.
* Returned the remaining common prefix.

#### Concepts Used

* Strings
* String Traversal
* Prefix Matching
* Horizontal Scanning

#### Time Complexity

* **O(n × m)**

#### Space Complexity

* **O(1)**

#### Example

```text id="sgg18c"
Input:  ["flower","flow","flight"]
Output: "fl"
```

---

## Programming Concepts

### Synchronous and Asynchronous Programming

**File:** `synchronous_and_asynchronous_programming.md`

#### Topics Covered

##### Synchronous Programming

* Tasks execute one after another.
* Each task waits for the previous task to finish.
* Easier to understand and debug.

##### Example

```python id="3hkw01"
print("Task 1")
print("Task 2")
print("Task 3")
```

Output:

```text id="e8a5vl"
Task 1
Task 2
Task 3
```

---

##### Asynchronous Programming

* Multiple tasks can progress without waiting for each other.
* Improves responsiveness and performance.
* Useful for I/O operations such as:

  * API Calls
  * Database Queries
  * File Operations

##### Example

```python id="47e9oq"
import asyncio

async def task():
    print("Task Started")
    await asyncio.sleep(2)
    print("Task Completed")

asyncio.run(task())
```

---

### Key Differences

| Synchronous               | Asynchronous                         |
| ------------------------- | ------------------------------------ |
| Sequential execution      | Concurrent execution                 |
| Blocking operations       | Non-blocking operations              |
| Simpler flow              | Better performance for I/O tasks     |
| Waits for task completion | Can perform other work while waiting |

---

## Repository Structure

```text id="z67rsl"
Day 4/
├── README.md
├── ContainerWithMostWater.java
├── LongestCommonPrefix.java
└── synchronous_and_asynchronous_programming.md
```

---

## Key Learnings

### DSA

* Learned how Two Pointers can reduce complexity from O(n²) to O(n).
* Understood why moving the smaller height pointer works in Container With Most Water.
* Practiced string comparison and prefix matching techniques.
* Improved understanding of optimization strategies.

### Programming Concepts

* Learned the difference between blocking and non-blocking execution.
* Understood when to use synchronous and asynchronous programming.
* Explored how asynchronous operations improve application performance.

---

## Progress Summary

✅ Container With Most Water

✅ Longest Common Prefix

✅ Synchronous Programming

✅ Asynchronous Programming
