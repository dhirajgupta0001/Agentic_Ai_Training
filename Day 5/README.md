# Asyncio Practice Notes

This document contains examples and explanations of common `asyncio` concepts in Python.

---

# 1. Sequential Execution with `await`

## Code

```python
from asyncio import run, sleep

async def job(delay):
    await sleep(delay)

async def main():
    await job(3)
    await job(2)
    await job(1)

run(main())
```

## What Happens?

The coroutines run one after another:

1. `job(3)` starts and sleeps for 3 seconds.
2. After it finishes, `job(2)` starts and sleeps for 2 seconds.
3. After it finishes, `job(1)` starts and sleeps for 1 second.

### Timeline

```text
0s -> job(3) starts
3s -> job(3) finishes

3s -> job(2) starts
5s -> job(2) finishes

5s -> job(1) starts
6s -> job(1) finishes
```

### Total Runtime

```text
3 + 2 + 1 = 6 seconds
```

### Important Note

`await` pauses the current coroutine but does **not** automatically start other coroutines.

---

# 2. Concurrent Execution with `gather`

## Code

```python
from asyncio import run, sleep, gather

async def job(delay):
    await sleep(delay)

async def main():
    await gather(
        job(3),
        job(2),
        job(1)
    )

run(main())
```

## What Happens?

All coroutines are scheduled concurrently.

### Timeline

```text
0s -> job(3), job(2), job(1) start
1s -> job(1) finishes
2s -> job(2) finishes
3s -> job(3) finishes
```

### Total Runtime

```text
3 seconds
```

The total runtime equals the longest-running coroutine.

---

# 3. Exception Inside `gather`

## Code

```python
from asyncio import sleep, run, gather

async def task1():
    await sleep(1)
    raise ValueError("Boom")

async def task2():
    await sleep(2)
    return 42

async def main():
    await gather(task1(), task2())

run(main())
```

## What Happens?

1. Both tasks start concurrently.
2. After 1 second, `task1()` raises `ValueError("Boom")`.
3. `gather()` immediately propagates the exception.
4. The program terminates with a traceback.

### Result

```text
ValueError: Boom
```

### Note

`task2()` does not return its value because the exception interrupts execution.

---

# 4. Handling Exceptions with `return_exceptions=True`

## Code

```python
from asyncio import run, gather

async def task1():
    raise ValueError("Bad")

async def task2():
    return 10

async def main():
    result = await gather(
        task1(),
        task2(),
        return_exceptions=True
    )
    print(result)

run(main())
```

## What Happens?

Instead of raising exceptions, `gather()` collects them as results.

### Output

```text
[ValueError('Bad'), 10]
```

### Explanation

The results are returned in the same order as the coroutines passed to `gather()`.

```python
[
    ValueError("Bad"),
    10
]
```

---

# Key Concepts Learned

## `await`

Suspends the current coroutine until the awaited operation completes.

Example:

```python
await sleep(3)
```

---

## `gather`

Runs multiple coroutines concurrently and waits for all of them.

Example:

```python
await gather(
    task1(),
    task2(),
    task3()
)
```

---

## Sequential vs Concurrent

### Sequential

```python
await task1()
await task2()
await task3()
```

Runtime:

```text
task1 + task2 + task3
```

### Concurrent

```python
await gather(
    task1(),
    task2(),
    task3()
)
```

Runtime:

```text
max(task1, task2, task3)
```

---

# Most Important Takeaway

A common misconception is:

> When a coroutine reaches `await`, other coroutines automatically start.

This is false.

A coroutine reaching `await` only gives control back to the event loop. Other coroutines can run only if they have already been scheduled (for example, using `gather()` or `create_task()`).

Therefore:

```python
await job(3)
await job(2)
await job(1)
```

is sequential,

while

```python
await gather(
    job(3),
    job(2),
    job(1)
)
```

is concurrent.
