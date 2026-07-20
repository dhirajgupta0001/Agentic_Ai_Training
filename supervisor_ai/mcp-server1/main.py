from fastmcp import FastMCP
import math

# Create MCP Server
mcp = FastMCP("Calculator_Server")


@mcp.tool()
def add(a: float, b: float) -> float:
    """Add two numbers."""
    return a + b


@mcp.tool()
def subtract(a: float, b: float) -> float:
    """Subtract two numbers."""
    return a - b


@mcp.tool()
def multiply(a: float, b: float) -> float:
    """Multiply two numbers."""
    return a * b


@mcp.tool()
def divide(a: float, b: float) -> float:
    """Divide two numbers."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


@mcp.tool()
def power(a: float, b: float) -> float:
    """Raise a number to a power."""
    return a ** b


@mcp.tool()
def square_root(a: float) -> float:
    """Calculate the square root."""
    if a < 0:
        raise ValueError("Cannot calculate square root of a negative number.")
    return math.sqrt(a)


if __name__ == "__main__":
    mcp.run()
