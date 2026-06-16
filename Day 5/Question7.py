from asyncio import run,sleep,gather

async def task1():
    raise ValueError("Bad")

async def task2():
    return 10

async def main():
    result=await gather(task1(),task2(),return_exceptions=True)
    print(result)

run(main())
