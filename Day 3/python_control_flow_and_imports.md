# Python Control Flow, Loops, Imports, Aliases, and Scope - Complete Guide

# Table of Contents

1. if Statement
2. if-else Statement
3. if-elif-else Statement
4. Nested if
5. for Loop
6. while Loop
7. break Statement
8. continue Statement
9. pass Statement
10. Importing Modules
11. Importing Functions from Other Files
12. Aliases using as
13. Scope in Python
14. Global vs Local Scope
15. LEGB Rule
16. Best Practices

---

# 1. if Statement

The `if` statement executes code only when a condition is True.

### Syntax

```python
if condition:
    statements
```

### Example

```python
age = 20

if age >= 18:
    print("Eligible to vote")
```

Output:

```text
Eligible to vote
```

---

# Comparison Operators

| Operator | Meaning               |
| -------- | --------------------- |
| ==       | Equal                 |
| !=       | Not Equal             |
| >        | Greater Than          |
| <        | Less Than             |
| >=       | Greater Than or Equal |
| <=       | Less Than or Equal    |

Example:

```python
x = 10

if x == 10:
    print("Matched")
```

---

# 2. if-else Statement

Used when there are two possible outcomes.

### Syntax

```python
if condition:
    statements
else:
    statements
```

### Example

```python
age = 15

if age >= 18:
    print("Adult")
else:
    print("Minor")
```

Output:

```text
Minor
```

---

# 3. if-elif-else Statement

Used when there are multiple conditions.

### Syntax

```python
if condition1:
    statements

elif condition2:
    statements

elif condition3:
    statements

else:
    statements
```

### Example

```python
marks = 75

if marks >= 90:
    print("Grade A")

elif marks >= 75:
    print("Grade B")

elif marks >= 60:
    print("Grade C")

else:
    print("Fail")
```

Output:

```text
Grade B
```

---

# 4. Nested if

An if statement inside another if statement.

```python
age = 25
citizen = True

if age >= 18:

    if citizen:
        print("Can vote")
```

Output:

```text
Can vote
```

---

# Logical Operators

| Operator | Meaning                      |
| -------- | ---------------------------- |
| and      | Both conditions must be True |
| or       | Any one condition True       |
| not      | Reverses condition           |

Example:

```python
age = 25
salary = 50000

if age > 18 and salary > 30000:
    print("Eligible")
```

---

# 5. for Loop

A for loop is used when we know how many times we want to iterate.

### Syntax

```python
for variable in iterable:
    statements
```

---

# Example 1

```python
for i in range(5):
    print(i)
```

Output:

```text
0
1
2
3
4
```

---

# range()

### range(stop)

```python
range(5)
```

Produces:

```text
0 1 2 3 4
```

---

### range(start, stop)

```python
for i in range(1, 6):
    print(i)
```

Output:

```text
1 2 3 4 5
```

---

### range(start, stop, step)

```python
for i in range(0, 10, 2):
    print(i)
```

Output:

```text
0 2 4 6 8
```

---

# Looping Through a List

```python
fruits = ["Apple", "Mango", "Orange"]

for fruit in fruits:
    print(fruit)
```

Output:

```text
Apple
Mango
Orange
```

---

# Looping Through a String

```python
for ch in "Python":
    print(ch)
```

Output:

```text
P
y
t
h
o
n
```

---

# 6. while Loop

Used when we don't know beforehand how many iterations are needed.

### Syntax

```python
while condition:
    statements
```

### Example

```python
count = 1

while count <= 5:
    print(count)
    count += 1
```

Output:

```text
1
2
3
4
5
```

---

# Infinite Loop

```python
while True:
    print("Running forever")
```

Usually stopped using break.

---

# 7. break Statement

Terminates the loop immediately.

### Example

```python
for i in range(10):

    if i == 5:
        break

    print(i)
```

Output:

```text
0
1
2
3
4
```

Loop stops when i becomes 5.

---

# break in while Loop

```python
count = 1

while True:

    if count == 5:
        break

    print(count)
    count += 1
```

Output:

```text
1
2
3
4
```

---

# 8. continue Statement

Skips the current iteration and moves to the next iteration.

### Example

```python
for i in range(5):

    if i == 2:
        continue

    print(i)
```

Output:

```text
0
1
3
4
```

Notice that 2 is skipped.

---

# 9. pass Statement

pass does nothing.

It is used as a placeholder when code is required syntactically but not yet implemented.

### Example

```python
if True:
    pass
```

---

# Example in Functions

```python
def future_feature():
    pass
```

Useful while designing programs.

---

# Importing Modules

A module is simply a Python file.

Example:

```text
math.py
student.py
employee.py
```

Each file is a module.

---

# 10. Basic Import

### math Module

```python
import math

print(math.sqrt(25))
```

Output:

```text
5.0
```

---

# Import Specific Function

```python
from math import sqrt

print(sqrt(25))
```

Output:

```text
5.0
```

No need to write math.sqrt()

---

# Import Multiple Functions

```python
from math import sqrt, factorial

print(sqrt(16))
print(factorial(5))
```

Output:

```text
4.0
120
```

---

# Import Everything (Not Recommended)

```python
from math import *
```

Avoid this because it pollutes the namespace.

---

# 11. Importing Your Own Python Files

Suppose we have:

## calculator.py

```python
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b
```

---

## main.py

```python
import calculator

print(calculator.add(10, 5))
print(calculator.subtract(10, 5))
```

Output:

```text
15
5
```

---

# Import Specific Function

```python
from calculator import add

print(add(5, 3))
```

Output:

```text
8
```

---

# Import Multiple Functions

```python
from calculator import add, subtract
```

---

# Project Structure

```text
project/
│
├── calculator.py
└── main.py
```

Files should be in the same directory.

---

# 12. Alias Using as

Alias means creating an alternative name.

### Syntax

```python
import module as alias
```

---

# Example 1

```python
import math as m

print(m.sqrt(25))
```

Output:

```text
5.0
```

Why?

Instead of repeatedly typing:

```python
math.sqrt()
math.factorial()
math.pow()
```

We can write:

```python
m.sqrt()
m.factorial()
m.pow()
```

---

# Function Alias

```python
from math import factorial as fact

print(fact(5))
```

Output:

```text
120
```

---

# Alias for Your Own Modules

```python
import calculator as calc

print(calc.add(10, 5))
```

Output:

```text
15
```

---

# Why Use Aliases?

1. Shorter code
2. Improves readability
3. Avoids naming conflicts

Example:

```python
import numpy as np
import pandas as pd
```

This is the industry standard.

---

# 13. Scope in Python

Scope determines where a variable can be accessed.

There are four scopes in Python.

---

# Local Scope

Variables created inside a function.

```python
def greet():
    message = "Hello"

    print(message)

greet()
```

Output:

```text
Hello
```

Outside the function:

```python
print(message)
```

Output:

```text
NameError
```

Because local variables exist only inside the function.

---

# Global Scope

Variables declared outside all functions.

```python
name = "Rahul"

def display():
    print(name)

display()
```

Output:

```text
Rahul
```

Global variables can be read inside functions.

---

# Modifying Global Variables

```python
count = 0

def update():
    global count

    count += 1

update()

print(count)
```

Output:

```text
1
```

Without global keyword Python creates a new local variable.

---

# 14. LEGB Rule

Python searches variables in this order:

### L → Local

Current function

### E → Enclosing

Outer function

### G → Global

Module level

### B → Built-in

Python built-in names

---

# Example

```python
x = "Global"

def outer():

    x = "Outer"

    def inner():
        x = "Inner"
        print(x)

    inner()

outer()
```

Output:

```text
Inner
```

Python found x in Local scope first.

---

# Enclosing Scope Example

```python
def outer():

    message = "Outer"

    def inner():
        print(message)

    inner()

outer()
```

Output:

```text
Outer
```

message belongs to the enclosing scope.

---

# Scope Importance

Scope helps:

1. Prevent variable conflicts
2. Improve memory management
3. Improve code readability
4. Improve security
5. Organize large projects

Without scope every variable would interfere with every other variable.

---

# Best Practices

✅ Use local variables whenever possible

```python
def calculate():
    result = 100
```

---

✅ Import only required functions

```python
from math import sqrt
```

---

✅ Use aliases for large libraries

```python
import numpy as np
import pandas as pd
```

---

❌ Avoid

```python
from math import *
```

---

❌ Avoid excessive global variables

```python
global data
```

Use functions and classes instead.

---

# Quick Summary

| Concept      | Purpose                         |
| ------------ | ------------------------------- |
| if           | Execute when condition is True  |
| else         | Execute when condition is False |
| elif         | Multiple conditions             |
| for          | Fixed iterations                |
| while        | Condition-based iterations      |
| break        | Stop loop                       |
| continue     | Skip iteration                  |
| pass         | Placeholder                     |
| import       | Load module                     |
| as           | Create alias                    |
| local scope  | Variable inside function        |
| global scope | Variable outside function       |
| LEGB         | Variable lookup rule            |
