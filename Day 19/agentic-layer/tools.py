from langchain_mcp_adapters.client import MultiServerMCPClient

async def get_tools():
    client=MultiServerMCPClient(
        {
            "Math's_Server":{
                "transport":"http",
                "url":"http://127.0.0.1:8002/mcp"
            },
            "Weather's_Server":{
                "transport":"http",
                "url":"http://127.0.0.1:8003/mcp"
            }
        }
    )
    return await client.get_tools()
