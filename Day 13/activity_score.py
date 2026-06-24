from github import get_github_user
from asyncio import run
async def calculate_activity_score(username: str):

    user = await get_github_user(username)

    followers = user["followers"]
    repos = user["public_repos"]

    score = followers * 2 + repos

    return {
        "username": username,
        "activity_score": score
    }
result=run(calculate_activity_score("dhirajgupta0001"))
print(result)
