from asyncio import sleep,run,gather

async def task1():
    await sleep(1)
    raise ValueError("Boom")

async def task2():
    await sleep(2)
    return 42

async def main():
    await gather(task1(),task2())

run(main())
