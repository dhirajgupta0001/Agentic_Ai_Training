# Python Classes and Object-Oriented Programming (OOP)

## Introduction

A **class** in Python is a blueprint for creating objects. It defines the data (attributes) and behavior (methods) that objects created from the class will have.

Classes are one of the fundamental concepts of **Object-Oriented Programming (OOP)** and help organize code into reusable and maintainable components.

---

# Real-World Analogy

Consider a blueprint for a house:

```text
Blueprint → Class
House     → Object
```

A blueprint describes how a house should look, but it is not an actual house.

Similarly:

* A class defines the structure.
* An object is an actual instance created from the class.

---

# What is a Class?

A class is a user-defined data type that contains:

* Attributes (variables)
* Methods (functions)

Basic syntax:

```python
class Person:
    pass
```

Here:

* `class` is the keyword used to define a class.
* `Person` is the class name.
* `pass` means no implementation yet.

---

# What is an Object?

An object is an instance of a class.

Example:

```python
class Person:
    pass

person1 = Person()

print(type(person1))
```

Output:

```text
<class '__main__.Person'>
```

`person1` is an object created from the `Person` class.

---

# Class Attributes

Attributes are variables associated with a class.

Example:

```python
class Person:
    name = "John"
    age = 25

person = Person()

print(person.name)
print(person.age)
```

Output:

```text
John
25
```

---

# The **init**() Method

The `__init__()` method is a constructor.

It is automatically executed when an object is created.

Example:

```python
class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

person = Person("Alice", 22)

print(person.name)
print(person.age)
```

Output:

```text
Alice
22
```

---

# Understanding self

`self` refers to the current object.

Example:

```python
class Person:

    def __init__(self, name):
        self.name = name
```

Object creation:

```python
person = Person("Alice")
```

Internally, Python does:

```python
Person.__init__(person, "Alice")
```

Therefore:

```text
self = person
```

---

# Instance Variables

Instance variables belong to individual objects.

Example:

```python
class Student:

    def __init__(self, name):
        self.name = name

s1 = Student("Rahul")
s2 = Student("Priya")

print(s1.name)
print(s2.name)
```

Output:

```text
Rahul
Priya
```

Each object has its own value for `name`.

---

# Methods

Methods are functions defined inside a class.

Example:

```python
class Person:

    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, my name is {self.name}")

person = Person("Alice")

person.greet()
```

Output:

```text
Hello, my name is Alice
```

---

# Class Variables

Class variables are shared among all objects.

Example:

```python
class Student:

    school = "ABC School"

s1 = Student()
s2 = Student()

print(s1.school)
print(s2.school)
```

Output:

```text
ABC School
ABC School
```

---

# Class Variables vs Instance Variables

```python
class Student:

    school = "ABC School"

    def __init__(self, name):
        self.name = name
```

| Type              | Example  | Shared? |
| ----------------- | -------- | ------- |
| Class Variable    | `school` | Yes     |
| Instance Variable | `name`   | No      |

---

# Example: Bank Account Class

```python
class BankAccount:

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def show_balance(self):
        print(f"Balance: {self.balance}")

account = BankAccount("Rahul", 1000)

account.deposit(500)
account.withdraw(200)

account.show_balance()
```

Output:

```text
Balance: 1300
```

---

# Object-Oriented Programming (OOP)

OOP is a programming paradigm based on objects and classes.

Four main principles:

1. Encapsulation
2. Inheritance
3. Polymorphism
4. Abstraction

---

# Encapsulation

Encapsulation means bundling data and methods together.

Example:

```python
class Car:

    def __init__(self):
        self.speed = 0
```

The object contains both data and behavior.

Benefits:

* Better organization
* Improved security
* Easier maintenance

---

# Inheritance

Inheritance allows one class to acquire properties and methods from another class.

Example:

```python
class Animal:

    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    pass

dog = Dog()

dog.speak()
```

Output:

```text
Animal speaks
```

Benefits:

* Code reuse
* Reduced duplication
* Easier extension

---

# Polymorphism

Polymorphism allows different classes to use the same method name.

Example:

```python
class Dog:

    def sound(self):
        print("Bark")

class Cat:

    def sound(self):
        print("Meow")
```

Usage:

```python
dog = Dog()
cat = Cat()

dog.sound()
cat.sound()
```

Output:

```text
Bark
Meow
```

---

# Abstraction

Abstraction hides implementation details and exposes only essential functionality.

Example:

```python
from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass
```

Benefits:

* Simpler interfaces
* Reduced complexity
* Better maintainability

---

# Special Methods (Dunder Methods)

Dunder means "double underscore."

Examples:

```python
__init__()
__str__()
__len__()
__repr__()
```

---

# **str**() Method

Controls how objects are displayed.

Example:

```python
class Person:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

p = Person("Alice")

print(p)
```

Output:

```text
Alice
```

---

# Object Lifecycle

```text
Class Definition
       ↓
Object Creation
       ↓
__init__()
       ↓
Attributes Initialized
       ↓
Methods Invoked
       ↓
Object Destroyed
```

---

# Best Practices

1. Use meaningful class names.
2. Follow PascalCase naming convention.

Example:

```python
class BankAccount:
    pass
```

3. Keep methods focused on one task.
4. Use inheritance carefully.
5. Encapsulate related functionality.
6. Prefer composition when appropriate.

---

# Common Naming Conventions

| Element  | Convention | Example           |
| -------- | ---------- | ----------------- |
| Class    | PascalCase | `BankAccount`     |
| Method   | snake_case | `show_balance()`  |
| Variable | snake_case | `account_balance` |
| Constant | UPPER_CASE | `MAX_USERS`       |

---

# Advantages of Classes

* Code reusability
* Better organization
* Easier maintenance
* Improved scalability
* Supports OOP principles
* Real-world modeling capability

---

# Interview Questions

### What is a class?

A class is a blueprint used to create objects.

### What is an object?

An object is an instance of a class.

### What is self?

`self` refers to the current object instance.

### What is **init**()?

It is a constructor method automatically called when an object is created.

### Difference between class and object?

| Class             | Object                  |
| ----------------- | ----------------------- |
| Blueprint         | Instance                |
| Defines structure | Contains actual data    |
| Created once      | Can have many instances |

---

# Interview Definition

A **class** in Python is a user-defined blueprint for creating objects. It encapsulates attributes (data) and methods (behavior) into a single unit and serves as the foundation of Object-Oriented Programming (OOP).

---

# One-Line Summary

**A class is a blueprint that defines data and behavior, while an object is a real instance created from that blueprint.**
