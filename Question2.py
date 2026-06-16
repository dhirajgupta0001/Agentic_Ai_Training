from asyncio import sleep,create_task,run

async def worker():
    print("Worker start")
    await sleep(1)
    print("worker end")

async def main():
    task=create_task(worker())
    print("main running")
    await task

run(main())
