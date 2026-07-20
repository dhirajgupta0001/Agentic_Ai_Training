from langchain_mcp_adapters.client import MultiServerMCPClient
async def get_tools():

    client = MultiServerMCPClient(
        {
            "Calculator_Server": {
                "transport": "http",
                "url":"http://127.0.0.1:8001/mcp"
            }
        }
    )

    return await client.get_tools()
