from fastmcp import Client
from asyncio import run
client=Client("http://127.0.0.1:8000/mcp")
# async def main():
#     async with client:
#         result =await client.call_tool(
#             "add",
#             {
#                 "x":10,
#                 "y":10
#             }
#         )
#         print(result)

async def main():
    async with client:
        result=await client.call_tool(
            "hello"
        )
        print(result.content[-1].text)

if __name__ == "__main__":
    run(main())
