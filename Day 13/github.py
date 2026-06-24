from httpx import AsyncClient
from asyncio import run
async def get_github_user(username: str):
    async with AsyncClient() as client:
      response = await client.get(
          f"https://api.github.com/users/{username}"
      )

      return response.json()

result=run(get_github_user('dhirajgupta0001'))
print(result)
