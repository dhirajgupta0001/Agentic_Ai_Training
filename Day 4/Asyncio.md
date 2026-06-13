# Python Synchronous and Asynchronous Programming - Complete Guide

# Table of Contents

1. What is Synchronous Programming?
2. What is Asynchronous Programming?
3. Why Async Programming Exists
4. Event Loop
5. Coroutine
6. async Keyword
7. await Keyword
8. run() Function
9. sleep() Function
10. Sequential Async Execution
11. Concurrent Async Execution
12. gather()
13. Returning Values from Coroutines
14. Async File Processing Example
15. Async Execution Flow
16. Common Mistakes
17. Best Practices
18. Interview Questions

---

# 1. What is Synchronous Programming?

In synchronous programming, tasks execute one after another.

The next task cannot start until the previous task completes.

Example:

```python
import time

def task1():
    time.sleep(3)
    print("Task1 Completed")

def task2():
    time.sleep(3)
    print("Task2 Completed")

task1()
task2()
```

Execution:

```text
Wait 3 seconds
Task1 Completed

Wait 3 seconds
Task2 Completed
```

Total Time:

```text
6 Seconds
```

Everything runs sequentially.

---

# 2. What is Asynchronous Programming?

Asynchronous programming allows tasks to pause and give control back to the event loop.

While one task is waiting, another task can run.

This improves performance for:

* APIs
* Databases
* Network Requests
* File Downloads
* Web Scraping
* Chat Applications

---

# 3. Why Async Programming Exists

Imagine:

```text
Task1 -> Wait 5 sec
Task2 -> Wait 5 sec
Task3 -> Wait 5 sec
```

Synchronous:

```text
5 + 5 + 5 = 15 sec
```

Async:

```text
5 sec total
```

Because all waiting happens together.

---

# 4. Event Loop

The Event Loop is the heart of asyncio.

It continuously checks:

```text
Is any task ready?
```

If yes:

```text
Execute it
```

If a task is waiting:

```text
Move to another task
```

Visual Representation:

```text
Event Loop
    |
    +---- Task1
    |
    +---- Task2
    |
    +---- Task3
```

The Event Loop manages all coroutines.

---

# 5. Coroutine

A coroutine is a special function that can pause execution.

Normal Function:

```python
def greet():
    print("Hello")
```

Coroutine:

```python
async def greet():
    print("Hello")
```

The coroutine does not execute immediately.

It returns a coroutine object.

---

# 6. async Keyword

Marks a function as asynchronous.

Example:

```python
async def hello():
    print("Hello")
```

Without async:

```python
def hello():
```

the function becomes synchronous.

---

# 7. await Keyword

await pauses the current coroutine.

Syntax:

```python
await something()
```

Meaning:

```text
Pause here
Let Event Loop run something else
Resume later
```

---

# Example

```python
from asyncio import run, sleep

async def hello():
    await sleep(2)
    print("Hello")
```

Execution:

```text
Pause 2 sec
Print Hello
```

---

# 8. run()

Starts the Event Loop.

Example:

```python
from asyncio import run

async def main():
    print("Hello")

run(main())
```

Without run():

```python
main()
```

Nothing executes properly because no event loop exists.

---

# 9. sleep()

Async version of time.sleep()

Wrong:

```python
import time

time.sleep(3)
```

Blocks entire program.

Correct:

```python
await sleep(3)
```

Only pauses current coroutine.

---

# Example 1 Analysis

Code:

```python
from asyncio import run,sleep

async def printMessage():
    print("Printing Message=> ")

    await helloIndia()

    print("India is the Best")

async def helloIndia():
    await sleep(2)

    print("hello India!!!")

run(printMessage())
```

Execution Flow:

```text
printMessage Starts

Printing Message=>

await helloIndia()

helloIndia Starts

wait 2 seconds

hello India!!!

return to printMessage

India is the Best
```

Output:

```text
Printing Message=>
(wait 2 sec)
hello India!!!
India is the Best
```

Execution Tree:

```text
printMessage
    |
    +-- helloIndia
```

---

# Example 2 Analysis

```python
task3
  |
  +--> task2
            |
            +--> task1
```

Code:

```python
await task2()
```

Inside task2:

```python
await task1()
```

Execution:

```text
task3 starts

task2 starts

task1 starts

wait 2 sec

task1

task2

wait 2 sec

task3
```

Output:

```text
task1
task2
task3
Tasks Completed!!!
```

Important:

This is still sequential execution.

There is NO concurrency.

Each task waits for previous task.

---

# Understanding Await Chaining

```python
await task1()
await task2()
await task3()
```

means:

```text
Run task1 completely

Then task2

Then task3
```

Equivalent to synchronous flow.

---

# Example 3 Analysis

```python
task3
    |
    +--> task2
              |
              +--> task1
```

Each function:

```python
await sleep(3)
```

Execution:

```text
task1 waits 3 sec

task2 waits 3 sec

task3 prints immediately
```

Total:

```text
6 seconds
```

Why?

Because:

```python
await task1()

await task2()
```

forces sequential execution.

---

# Example 4 - gather()

This is where real async happens.

```python
await gather(
    task1(),
    task2(),
    task3()
)
```

All coroutines start together.

Execution:

```text
task1 starts
task2 starts
task3 starts

all sleep simultaneously

all wake together
```

Output:

```text
Message
Message
Message
```

Total Time:

```text
3 seconds
```

instead of:

```text
9 seconds
```

This is called Concurrent Execution.

---

# How gather() Works

Without gather:

```python
await task1()
await task2()
await task3()
```

Time:

```text
3 + 3 + 3 = 9 sec
```

With gather:

```python
await gather(
    task1(),
    task2(),
    task3()
)
```

Time:

```text
3 sec
```

Because all waiting happens simultaneously.

---

# Example 5 - Returning Values

Code:

```python
result1 = await task1()
result2 = await task2(result1)
result3 = await task3(result2)
```

This creates a pipeline.

Execution:

```text
task1

returns:
test1

task2 receives:
test1

returns:
test1 test2

task3 receives:
test1 test2

returns:
test1 test2 test3
```

Output:

```text
test1 test2 test3
```

---

# Async Return Values

Example:

```python
async def get_name():
    return "Dhiraj"
```

Usage:

```python
name = await get_name()
```

Output:

```text
Dhiraj
```

---

# Async Execution Flow

```text
run(main())

        |
        v

Event Loop Starts

        |
        v

Coroutine Scheduled

        |
        v

Coroutine Executes

        |
        v

await Found

        |
        v

Coroutine Paused

        |
        v

Event Loop Executes Others

        |
        v

Coroutine Resumes

        |
        v

Returns Result
```

---

# Common Mistakes

## Mistake 1

```python
await outside async
```

Wrong:

```python
await sleep(1)
```

Correct:

```python
async def test():
    await sleep(1)
```

---

## Mistake 2

```python
time.sleep()
```

inside async code.

Wrong:

```python
time.sleep(3)
```

Correct:

```python
await sleep(3)
```

---

## Mistake 3

Forgetting await

Wrong:

```python
task1()
```

Correct:

```python
await task1()
```

---

# When To Use Async

Use Async For:

✅ HTTP Requests

✅ APIs

✅ Database Calls

✅ Downloads

✅ Uploads

✅ Web Scraping

✅ Socket Programming

---

# When NOT To Use Async

Avoid Async For:

❌ Heavy Calculations

❌ Image Processing

❌ Machine Learning Training

❌ CPU Intensive Tasks

For those use:

```python
multiprocessing
```

or

```python
threading
```

depending on use case.

---

# Best Practices

### Use gather for independent tasks

```python
await gather(
    task1(),
    task2(),
    task3()
)
```

---

### Use await chaining for dependent tasks

```python
result1 = await task1()
result2 = await task2(result1)
result3 = await task3(result2)
```

---

### Never use time.sleep inside async code

Use:

```python
await sleep()
```

---

### Keep coroutines small and focused

Good:

```python
async def fetch_user():
```

Bad:

```python
async def everything():
```

---

# Quick Summary

| Concept     | Purpose                |
| ----------- | ---------------------- |
| async       | Creates coroutine      |
| await       | Pause coroutine        |
| run()       | Starts event loop      |
| sleep()     | Non-blocking delay     |
| gather()    | Run tasks concurrently |
| coroutine   | Async function         |
| event loop  | Scheduler              |
| return      | Return async result    |
| await chain | Sequential dependency  |
| gather      | Parallel waiting       |

---

# Interview One-Liner

Synchronous programming executes tasks one after another, whereas asynchronous programming allows tasks to pause during waiting operations and enables the event loop to execute other tasks concurrently, improving the efficiency of I/O-bound applications.
