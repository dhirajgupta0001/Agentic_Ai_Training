from asyncio import run
from github import get_repositories
async def primary_skill(username:str):
    repos=await get_repositories(username)
    languages={}
    for repo in repos:
        language=repo["language"]
        if language is None:
            continue
        if language not in languages:
            languages[language]=1
        else: 
            languages[language] += 1
    
    primary_skill=max(languages,key=languages.get)
    return {
        "username": username,
        "primary_skill": primary_skill,
        "language_distribution": languages
    }
result=run(primary_skill('dhirajgupta0001'))
print(result)
