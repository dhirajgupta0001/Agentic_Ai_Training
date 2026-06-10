# Python Exception Handling - Complete Guide with Examples

## What is an Exception?

An exception is an error that occurs during the execution of a program. If not handled properly, it can terminate the program.

Example:

```python
x = 10 / 0
```

Output:

```text
ZeroDivisionError: division by zero
```

---

# Exception Handling Keywords

Python provides the following keywords for exception handling:

* `try`
* `except`
* `else`
* `finally`
* `raise`

---

# 1. try Block

The `try` block contains code that may generate an exception.

### Syntax

```python
try:
    # risky code
```

### Example

```python
try:
    num = int(input("Enter a number: "))
    print(num)
except:
    print("An error occurred")
```

---

# 2. except Block

The `except` block handles exceptions that occur inside the `try` block.

### Example

```python
try:
    result = 10 / 0

except ZeroDivisionError:
    print("Cannot divide by zero")
```

Output:

```text
Cannot divide by zero
```

---

# 3. Multiple except Blocks

Different exceptions can be handled separately.

```python
try:
    num = int(input("Enter a number: "))
    result = 100 / num

except ValueError:
    print("Invalid number")

except ZeroDivisionError:
    print("Cannot divide by zero")
```

---

# 4. Multiple Exceptions in One Block

```python
try:
    num = int(input("Enter a number: "))
    result = 100 / num

except (ValueError, ZeroDivisionError):
    print("Input error occurred")
```

---

# 5. Generic Exception Handling

```python
try:
    number = int("hello")

except Exception:
    print("Some error occurred")
```

---

# 6. Accessing Error Information

Use `as` to capture exception details.

```python
try:
    int("abc")

except ValueError as e:
    print("Error:", e)
```

Output:

```text
Error: invalid literal for int() with base 10: 'abc'
```

---

# 7. else Block

The `else` block executes only if no exception occurs.

### Syntax

```python
try:
    pass

except:
    pass

else:
    pass
```

### Example

```python
try:
    result = 10 / 2

except ZeroDivisionError:
    print("Division Error")

else:
    print("Result:", result)
```

Output:

```text
Result: 5.0
```

---

# 8. finally Block

The `finally` block always executes whether an exception occurs or not.

### Example

```python
try:
    result = 10 / 0

except ZeroDivisionError:
    print("Division by zero")

finally:
    print("Execution completed")
```

Output:

```text
Division by zero
Execution completed
```

---

# 9. Complete Exception Structure

```python
try:
    num = int(input("Enter a number: "))
    result = 100 / num

except ValueError:
    print("Invalid input")

except ZeroDivisionError:
    print("Cannot divide by zero")

else:
    print("Result:", result)

finally:
    print("Program finished")
```

---

# 10. Nested try-except

```python
try:
    print("Outer try")

    try:
        result = 10 / 0

    except ZeroDivisionError:
        print("Inner exception handled")

except:
    print("Outer exception handled")
```

Output:

```text
Outer try
Inner exception handled
```

---

# 11. raise Statement

The `raise` keyword is used to generate exceptions manually.

### Example

```python
age = -5

if age < 0:
    raise ValueError("Age cannot be negative")
```

Output:

```text
ValueError: Age cannot be negative
```

---

# 12. Custom Exceptions

Custom exceptions can be created by inheriting from the Exception class.

### Example

```python
class InvalidAgeError(Exception):
    pass

try:
    age = -10

    if age < 0:
        raise InvalidAgeError("Negative age not allowed")

except InvalidAgeError as e:
    print(e)
```

Output:

```text
Negative age not allowed
```

---

# Common Python Exceptions

## 1. ZeroDivisionError

Occurs when dividing by zero.

```python
try:
    print(10 / 0)

except ZeroDivisionError:
    print("Cannot divide by zero")
```

---

## 2. ValueError

Occurs when an invalid value is supplied.

```python
try:
    num = int("abc")

except ValueError:
    print("Invalid conversion")
```

---

## 3. TypeError

Occurs when operations are performed on incompatible types.

```python
try:
    result = "10" + 5

except TypeError:
    print("Type mismatch")
```

---

## 4. IndexError

Occurs when accessing an invalid list index.

```python
try:
    numbers = [1, 2, 3]
    print(numbers[10])

except IndexError:
    print("Index out of range")
```

---

## 5. KeyError

Occurs when a dictionary key is not found.

```python
try:
    student = {"name": "John"}
    print(student["age"])

except KeyError:
    print("Key not found")
```

---

## 6. NameError

Occurs when a variable is not defined.

```python
try:
    print(username)

except NameError:
    print("Variable not defined")
```

---

## 7. AttributeError

Occurs when an object does not have a requested attribute.

```python
try:
    text = "Python"
    text.append("A")

except AttributeError:
    print("Attribute does not exist")
```

---

## 8. FileNotFoundError

Occurs when a file cannot be located.

```python
try:
    file = open("sample.txt")

except FileNotFoundError:
    print("File not found")
```

---

## 9. ImportError

Occurs when importing a module fails.

```python
try:
    import nonexistent_module

except ImportError:
    print("Module not found")
```

---

## 10. ModuleNotFoundError

Occurs when a module does not exist.

```python
try:
    import abcxyz

except ModuleNotFoundError:
    print("Module does not exist")
```

---

## 11. OverflowError

Occurs when a numerical operation exceeds limits.

```python
import math

try:
    print(math.exp(1000))

except OverflowError:
    print("Number too large")
```

---

## 12. RecursionError

Occurs when recursion exceeds maximum depth.

```python
def test():
    test()

try:
    test()

except RecursionError:
    print("Maximum recursion depth exceeded")
```

---

## 13. AssertionError

Occurs when an assertion fails.

```python
try:
    assert 5 > 10

except AssertionError:
    print("Assertion failed")
```

---

## 14. KeyboardInterrupt

Occurs when the user interrupts execution using Ctrl+C.

```python
try:
    while True:
        pass

except KeyboardInterrupt:
    print("Program interrupted")
```

---

# Exception Hierarchy

```text
BaseException
│
├── SystemExit
├── KeyboardInterrupt
├── GeneratorExit
│
└── Exception
    ├── ArithmeticError
    │   ├── ZeroDivisionError
    │   ├── OverflowError
    │   └── FloatingPointError
    │
    ├── LookupError
    │   ├── IndexError
    │   └── KeyError
    │
    ├── ValueError
    ├── TypeError
    ├── NameError
    ├── AttributeError
    ├── ImportError
    ├── FileNotFoundError
    └── RuntimeError
```

---

# Best Practices

## Good Practice

```python
try:
    file = open("data.txt")

except FileNotFoundError:
    print("File not found")
```

Handle specific exceptions whenever possible.

---

## Avoid

```python
try:
    file = open("data.txt")

except:
    pass
```

Never silently ignore exceptions.

---

## Use finally for Cleanup

```python
file = None

try:
    file = open("data.txt")

except FileNotFoundError:
    print("File not found")

finally:
    if file:
        file.close()
```

---

# Summary

| Keyword | Purpose                         |
| ------- | ------------------------------- |
| try     | Contains risky code             |
| except  | Handles exceptions              |
| else    | Executes if no exception occurs |
| finally | Always executes                 |
| raise   | Generates exceptions manually   |

Exception handling helps create robust, maintainable, and production-ready Python applications.
