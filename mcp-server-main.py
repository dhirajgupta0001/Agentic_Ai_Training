from fastmcp import FastMCP

mcp=FastMCP("Simple Server")

@mcp.tool
def hello():
    return "Hello, World!"

@mcp.tool
def add(x:int,y:int):
    return x+y

@mcp.tool
def multiply(x:int,y:int):
    return x*y

@mcp.tool
def sub(x:int,y:int):
    return x-y
    
if __name__ == "__main__":
    mcp.run()

