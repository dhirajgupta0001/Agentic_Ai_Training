from asyncio import run,sleep,create_task

async def foo():
    print('A')
    await sleep(0)
    print('B')

async def main():
    task=create_task(foo())
    print('C')
    await task
    print('D')

run(main())
