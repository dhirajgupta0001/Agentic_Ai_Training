from asyncio import run,sleep

async def job(delay):
    await sleep(delay)

async def main():
    await job(3)
    await job(2)
    await job(1)

run(main())
