import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import create_agent

from tools import(
    create_user,
    get_user,
    update_user,
    delete_user,
    list_users,
    search_users,
)

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY"),
    temperature=0,
)

tools = [
    create_user,
    get_user,
    update_user,
    delete_user,
    list_users,
    search_users,
]

agent = create_agent(
    model=model,
    tools=tools,
    system_prompt="""
You are a helpful assistant.

Whenever possible use the available tools.

Never invent user information.

If the user asks to:

- create a user → use create_user
- update a user → use update_user
- delete a user → use delete_user
- search users → use search_users
- list users → use list_users
- fetch a user → use get_user

Always use the tools.
""",
)
