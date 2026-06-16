from asyncio import run,sleep,create_task,CancelledError

async def worker():
    try:
        while True:
            print("working")
            await sleep(1)
    except CancelledError:
        print("cancelled")
        raise

async def main():
    task=create_task(worker())
    await sleep(2.5)
    task.cancel()

    try:
        await task
    except CancelledError:
        print("main noticed")

run(main())
