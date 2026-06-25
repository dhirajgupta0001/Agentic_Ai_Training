from asyncio import run
from github import get_repositories

async def top_repository(username:str):
    repos=await get_repositories(username)
    top_repo=repos[0]

    for repo in repos:
        if repo["stargazers_count"] > top_repo["stargazers_count"]:
            top_repo=repo
    return{
        "repository": top_repo["name"],
        "stars": top_repo["stargazers_count"]
    }
result=run(top_repository('dhirajgupta0001'))
print(result)
