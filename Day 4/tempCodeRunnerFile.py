from asyncio import run,sleep,gather
async def task1():
    with open("/Users/dhirajgupta/Developer/Code/Agentic_Ai/Python/test.txt",'r',-1,'utf-8') as file:
        message=file.read()
        await sleep(3)
        print(message)
        return 'test1'

async def task2(test):
    with open("/Users/dhirajgupta/Developer/Code/Agentic_Ai/Python/test.txt",'r',-1,'utf-8') as file:
        message=file.read()
        await sleep(3)
        print(message)
        return test+ ' ' + 'test2'

async def task3(test):
    with open("/Users/dhirajgupta/Developer/Code/Agentic_Ai/Python/test.txt",'r',-1,'utf-8') as file:
        message=file.read()
        await sleep(3)
        print(message)
        return test+ ' ' + 'test3'

async def main():
    result1=await task1()
    result2=await task2(result1)
    result3=await task3(result2)
    print(result3)

run(main())
print("Tasks Completed!!!")
