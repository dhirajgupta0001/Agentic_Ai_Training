from asyncio import run,sleep,gather

async def job(delay):
    await sleep(delay)

async def main():
    await gather(job(3),job(2),job(1))

run(main())
  
