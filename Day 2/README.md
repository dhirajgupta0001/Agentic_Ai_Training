## Problems Solved

### 1. Longest Substring Without Repeating Characters

**File:** `LengthOfLongestSubstring.java`

#### Problem Statement

Given a string `s`, find the length of the longest substring without repeating characters.

#### Approach

* Used the **Sliding Window** technique.
* Maintained a window of unique characters using a `HashSet`.
* Expanded the window using a right pointer.
* Shrank the window whenever a duplicate character was found.
* Updated the maximum length encountered.

#### Concepts Used

* Sliding Window
* Two Pointers
* HashSet
* String Manipulation

#### Time Complexity

* **O(n)**

#### Space Complexity

* **O(n)**

---

### 2. Roman to Integer

**File:** `RomanToInteger.java`

#### Problem Statement

Convert a Roman numeral into its corresponding integer value.

#### Approach

* Stored Roman numeral values in a `HashMap`.
* Traversed the string from left to right.
* If the current value was smaller than the next value, subtracted it.
* Otherwise, added it to the result.

#### Concepts Used

* HashMap
* String Traversal
* Conditional Logic

#### Time Complexity

* **O(n)**

#### Space Complexity

* **O(1)**

---

## Python Learning

### Python Exceptions

**File:** `python_exceptions.md`

#### Topics Covered

* What are exceptions?
* Common built-in exceptions:

  * `ValueError`
  * `TypeError`
  * `IndexError`
  * `KeyError`
  * `ZeroDivisionError`
  * `FileNotFoundError`
* Using `try`, `except`, `else`, and `finally`
* Raising custom exceptions with `raise`
* Exception handling best practices

#### Example

```python
try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ZeroDivisionError:
    print("Cannot divide by zero.")
except ValueError:
    print("Invalid input.")
finally:
    print("Execution completed.")
```

---

## Key Learnings

### Problem Solving

* Improved understanding of sliding window algorithms.
* Learned efficient string processing techniques.
* Practiced working with HashMap and HashSet data structures.

### Python

* Learned how exceptions help prevent program crashes.
* Practiced handling runtime errors gracefully.
* Understood the importance of robust error handling.

---

## Repository Structure

```text
.
├── LengthOfLongestSubstring.java
├── RomanToInteger.java
├── python_exceptions.md
└── README.md
```

---

## Goals

* Solve coding problems consistently.
* Strengthen Data Structures and Algorithms knowledge.
* Learn Python concepts alongside Java development.
* Maintain a record of daily progress and learning outcomes.

---

### Progress Summary

✅ Longest Substring Without Repeating Characters
✅ Roman to Integer
✅ Python Exceptions
