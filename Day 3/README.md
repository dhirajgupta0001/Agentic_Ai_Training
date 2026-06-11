## Problems Solved

### 1. Longest Palindromic Substring

**File:** `LongestPalindromicSubstring.java`

#### Problem Statement

Given a string `s`, return the longest palindromic substring in `s`.

#### Approach

* Used the **Expand Around Center** technique.
* Considered every character as a potential center.
* Checked both:

  * Odd-length palindromes (e.g., `aba`)
  * Even-length palindromes (e.g., `abba`)
* Expanded outward while characters matched.
* Tracked the longest palindrome found.

#### Concepts Used

* Strings
* Two Pointers
* Expand Around Center
* Palindrome Detection

#### Time Complexity

* **O(n²)**

#### Space Complexity

* **O(1)**

#### Example

```text id="gfqux4"
Input:  "babad"
Output: "bab"

Explanation:
Both "bab" and "aba" are valid answers.
```

---

## Python Learning

### Python Control Flow and Imports

**File:** `python_control_flow_and_imports.md`

#### Topics Covered

##### Control Flow

* if statements
* if-else statements
* if-elif-else ladder
* Nested conditions
* for loops
* while loops
* break statement
* continue statement
* pass statement

##### Imports

* Importing modules
* Importing specific functions
* Using aliases
* Built-in modules

#### Examples

##### Control Flow

```python id="z5lh1k"
age = 20

if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible")
```

##### Importing Modules

```python id="vd6zrl"
import math

print(math.sqrt(25))
```

##### Importing Specific Functions

```python id="0lr7uy"
from math import sqrt

print(sqrt(25))
```

##### Using Aliases

```python id="8cb5dd"
import numpy as np
```

---

## Repository Structure

```text id="2sw9ko"
Day 3/
├── README.md
├── LongestPalindromicSubstring.java
└── python_control_flow_and_imports.md
```

---

## Key Learnings

### DSA

* Understood how palindromes expand around a center.
* Learned the difference between odd and even length palindromes.
* Improved string traversal and two-pointer techniques.

### Python

* Learned decision-making and looping constructs.
* Practiced controlling program execution flow.
* Understood how modules and imports improve code reusability.

---

## Progress Summary

✅ Longest Palindromic Substring

✅ Python Control Flow

✅ Python Imports
