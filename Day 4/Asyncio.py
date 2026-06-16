from asyncio import run,sleep
async def printMessage():
    print("Printing Message=> ")
    await helloIndia()
    print("India is the Best")

async def helloIndia():
    await sleep(2)
    print("hello India!!!")

run(printMessage())
