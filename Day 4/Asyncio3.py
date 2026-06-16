from asyncio import run,sleep
async def task1():
    with open("/Users/dhirajgupta/Developer/Code/Agentic_Ai/Python/test.txt",'r',-1,'utf-8') as file:
        message=file.read()
        await sleep(3)
        print(message)

async def task2():
    await task1()
    with open("/Users/dhirajgupta/Developer/Code/Agentic_Ai/Python/test.txt",'r',-1,'utf-8') as file:
        message=file.read()
        await sleep(3)
        print(message)

async def task3():
    await task2()
    with open("/Users/dhirajgupta/Developer/Code/Agentic_Ai/Python/test.txt",'r',-1,'utf-8') as file:
        message=file.read()
        print(message)

run(task3())
print("Tasks Completed!!!")
