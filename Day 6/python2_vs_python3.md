# Python 2 vs Python 3

## Introduction

Python is a popular high-level programming language known for its simplicity and readability. Python 2 and Python 3 are two major versions of the language. Python 2 was widely used for many years, but it reached its end of life on January 1, 2020. Python 3 is the current and actively maintained version.

## Key Differences

| Feature            | Python 2               | Python 3                   |
| ------------------ | ---------------------- | -------------------------- |
| Print Statement    | `print "Hello"`        | `print("Hello")`           |
| Division           | `5 / 2` returns `2`    | `5 / 2` returns `2.5`      |
| Unicode Support    | ASCII by default       | Unicode by default         |
| Input Function     | `raw_input()`          | `input()`                  |
| Range Function     | Returns a list         | Returns an iterable object |
| Exception Handling | `except Exception, e:` | `except Exception as e:`   |
| Dictionary Methods | Return lists           | Return view objects        |
| Support Status     | Ended in 2020          | Actively maintained        |

## 1. Print Function

### Python 2

```python
print "Hello, World!"
```

### Python 3

```python
print("Hello, World!")
```

Python 3 treats `print` as a function, making it more consistent and flexible.

---

## 2. Division Behavior

### Python 2

```python
print(5 / 2)    # Output: 2
print(5.0 / 2)  # Output: 2.5
```

### Python 3

```python
print(5 / 2)    # Output: 2.5
print(5 // 2)   # Output: 2
```

Python 3 performs true division by default.

---

## 3. Input Functions

### Python 2

```python
name = raw_input("Enter your name: ")
```

### Python 3

```python
name = input("Enter your name: ")
```

Python 3 simplifies user input by using a single `input()` function.

---

## 4. Unicode Support

### Python 2

```python
text = u"Hello"
```

### Python 3

```python
text = "Hello"
```

Strings in Python 3 are Unicode by default, making international text handling easier.

---

## 5. Range Function

### Python 2

```python
numbers = range(1000000)
```

This creates a complete list in memory.

### Python 3

```python
numbers = range(1000000)
```

This creates a lazy iterable, which is more memory efficient.

---

## 6. Exception Handling

### Python 2

```python
try:
    pass
except Exception, e:
    print(e)
```

### Python 3

```python
try:
    pass
except Exception as e:
    print(e)
```

The Python 3 syntax is clearer and more consistent.

---

## 7. Dictionary Methods

### Python 2

```python
data = {"a": 1, "b": 2}
print(data.keys())
```

Returns a list.

### Python 3

```python
data = {"a": 1, "b": 2}
print(data.keys())
```

Returns a view object that updates dynamically.

---

## Why Python 3 is Preferred

* Actively maintained and updated.
* Better Unicode support.
* Improved performance and memory management.
* Enhanced standard library.
* Supported by modern frameworks and libraries.
* Recommended for all new projects.

## Conclusion

Python 3 is the modern version of Python and should be used for all new development. Python 2 is obsolete and should only be used when maintaining legacy applications that cannot be migrated.

**Recommendation:** Learn and use Python 3 for all future projects.
