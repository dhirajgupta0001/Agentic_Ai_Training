from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import create_agent
from tools import calc

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key="Api_key",
    temperature=0.7,
)

agent = create_agent(
    model=model,
    tools=[calc],
    system_prompt="""You are a helpful assistant.
Use the appropriate tool."""
)


