from asyncio import run,sleep,gather
async def task1():
    with open("/Users/dhirajgupta/Developer/Code/Agentic_Ai/Python/test.txt",'r',-1,'utf-8') as file:
        message=file.read()
        await sleep(3)
        print(message)

async def task2():
    with open("/Users/dhirajgupta/Developer/Code/Agentic_Ai/Python/test.txt",'r',-1,'utf-8') as file:
        message=file.read()
        await sleep(3)
        print(message)

async def task3():
    with open("/Users/dhirajgupta/Developer/Code/Agentic_Ai/Python/test.txt",'r',-1,'utf-8') as file:
        message=file.read()
        await sleep(3)
        print(message)

async def main():
    await gather(task1(),task2(),task3())

run(main())
print("Tasks Completed!!!")
