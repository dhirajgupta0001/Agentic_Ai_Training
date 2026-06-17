# Shallow Copy vs Deep Copy in Python

## Introduction

In Python, variables store references to objects rather than the actual objects themselves. When working with mutable objects such as lists, dictionaries, and custom class instances, understanding how copying works is essential.

Python provides two main ways to copy objects:

1. **Shallow Copy**
2. **Deep Copy**

The primary difference lies in how nested objects are handled.

---

# Why Do We Need Copying?

Consider the following example:

```python
a = [1, 2, 3]

b = a

b[0] = 100

print(a)
```

Output:

```python
[100, 2, 3]
```

Why?

Because both variables reference the same object.

Memory representation:

```text
a ──┐
    ├── [1, 2, 3]
b ──┘
```

Any modification through one reference affects the other.

To create independent objects, we use copying.

---

# What is a Shallow Copy?

A shallow copy creates:

* A new outer object
* References to the same nested objects

Python's `copy.copy()` function creates a shallow copy.

Example:

```python
import copy

original = [[1, 2], [3, 4]]

shallow = copy.copy(original)

print(original is shallow)
```

Output:

```python
False
```

The outer list is different.

---

# Memory Structure of Shallow Copy

```text
original ──► [ A , B ]
               │   │
               ▼   ▼
            [1,2][3,4]

shallow  ──► [ A , B ]
```

Notice:

* Outer list is copied.
* Inner lists are shared.

---

# Modifying Nested Objects in Shallow Copy

Example:

```python
import copy

original = [[1, 2], [3, 4]]

shallow = copy.copy(original)

shallow[0][0] = 100

print(original)
print(shallow)
```

Output:

```python
[[100, 2], [3, 4]]
[[100, 2], [3, 4]]
```

Both objects change because the nested list is shared.

---

# Modifying the Outer Object

Example:

```python
import copy

original = [[1, 2], [3, 4]]

shallow = copy.copy(original)

shallow.append([5, 6])

print(original)
print(shallow)
```

Output:

```python
[[1, 2], [3, 4]]
[[1, 2], [3, 4], [5, 6]]
```

The outer list is independent.

---

# What is a Deep Copy?

A deep copy creates:

* A new outer object
* New copies of all nested objects

Python's `copy.deepcopy()` function performs a deep copy.

Example:

```python
import copy

original = [[1, 2], [3, 4]]

deep = copy.deepcopy(original)
```

---

# Memory Structure of Deep Copy

```text
original ──► [ A , B ]
               │   │
               ▼   ▼
            [1,2][3,4]

deep     ──► [ C , D ]
               │   │
               ▼   ▼
            [1,2][3,4]
```

Everything is copied.

No objects are shared.

---

# Modifying Nested Objects in Deep Copy

Example:

```python
import copy

original = [[1, 2], [3, 4]]

deep = copy.deepcopy(original)

deep[0][0] = 100

print(original)
print(deep)
```

Output:

```python
[[1, 2], [3, 4]]
[[100, 2], [3, 4]]
```

The original remains unchanged.

---

# Shallow Copy vs Deep Copy Example

```python
import copy

original = [[1, 2], [3, 4]]

shallow = copy.copy(original)
deep = copy.deepcopy(original)

shallow[0][0] = 999

print("Original:", original)
print("Shallow :", shallow)
print("Deep    :", deep)
```

Output:

```python
Original: [[999, 2], [3, 4]]
Shallow : [[999, 2], [3, 4]]
Deep    : [[1, 2], [3, 4]]
```

---

# Ways to Create a Shallow Copy

## Using copy.copy()

```python
import copy

new_list = copy.copy(old_list)
```

---

## Using List Slicing

```python
new_list = old_list[:]
```

---

## Using list()

```python
new_list = list(old_list)
```

---

## Using copy() Method

```python
new_list = old_list.copy()
```

All of these create shallow copies.

---

# Shallow Copy with Dictionaries

Example:

```python
import copy

student = {
    "name": "John",
    "marks": [80, 90]
}

shallow = copy.copy(student)

shallow["marks"][0] = 100

print(student)
```

Output:

```python
{
    'name': 'John',
    'marks': [100, 90]
}
```

The nested list is shared.

---

# Deep Copy with Dictionaries

Example:

```python
import copy

student = {
    "name": "John",
    "marks": [80, 90]
}

deep = copy.deepcopy(student)

deep["marks"][0] = 100

print(student)
print(deep)
```

Output:

```python
{
    'name': 'John',
    'marks': [80, 90]
}

{
    'name': 'John',
    'marks': [100, 90]
}
```

The objects are completely independent.

---

# Deep Copy with Custom Classes

Example:

```python
import copy

class Person:

    def __init__(self, name, hobbies):
        self.name = name
        self.hobbies = hobbies

p1 = Person(
    "Alice",
    ["Reading"]
)

p2 = copy.deepcopy(p1)

p2.hobbies.append("Coding")

print(p1.hobbies)
print(p2.hobbies)
```

Output:

```python
['Reading']
['Reading', 'Coding']
```

The copied object is independent.

---

# Performance Comparison

| Feature                  | Shallow Copy | Deep Copy |
| ------------------------ | ------------ | --------- |
| Copies outer object      | Yes          | Yes       |
| Copies nested objects    | No           | Yes       |
| Memory usage             | Lower        | Higher    |
| Execution speed          | Faster       | Slower    |
| Shared nested references | Yes          | No        |
| Complete independence    | No           | Yes       |

---

# When to Use Shallow Copy

Use shallow copy when:

* Objects are simple.
* Nested objects do not need to be independent.
* Performance is important.
* Shared nested data is acceptable.

Example:

```python
users = ["Alice", "Bob"]

backup = users.copy()
```

---

# When to Use Deep Copy

Use deep copy when:

* Objects contain nested mutable structures.
* Complete independence is required.
* Modifying one copy should never affect another.

Example:

```python
company_data = {
    "employees": [
        {"name": "John"}
    ]
}
```

Deep copy is preferred here.

---

# Visual Comparison

## Shallow Copy

```text
Original
   │
   ▼
[ List ]
   │
   ▼
[Nested List]

Copy
   │
   ▼
[ New List ]
   │
   ▼
[Nested List]  ← Shared
```

---

## Deep Copy

```text
Original
   │
   ▼
[ List ]
   │
   ▼
[Nested List]

Copy
   │
   ▼
[ New List ]
   │
   ▼
[ New Nested List ]
```

---

# Common Interview Questions

## What is a shallow copy?

A shallow copy creates a new object but shares references to nested objects.

---

## What is a deep copy?

A deep copy recursively copies all nested objects, creating a completely independent structure.

---

## Which module provides copy functionality?

```python
import copy
```

Functions:

```python
copy.copy()
copy.deepcopy()
```

---

## Which is faster?

Shallow copy is generally faster because it copies only the outer object.

---

## Which uses more memory?

Deep copy uses more memory because it duplicates all nested objects.

---

# Interview Definition

### Shallow Copy

A shallow copy creates a new object but copies references to nested objects. Changes to nested mutable objects affect both the original and copied objects.

### Deep Copy

A deep copy creates a completely independent copy of an object, including all nested objects. Changes to the copied object do not affect the original object.

---

# One-Line Summary

**Shallow copy duplicates only the outer container and shares nested objects, whereas deep copy recursively duplicates the entire object hierarchy, making all objects independent.**
