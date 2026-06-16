from asyncio import run,sleep,gather

async def task(name):
    print(f"{name} started")
    await sleep(2)
    print(f"{name} finished")

async def main():
    await gather(
        task("A"),
        task("B"),
        task("C")
    )

run(main())
