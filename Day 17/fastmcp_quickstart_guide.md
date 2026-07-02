# FastMCP Quickstart Guide

## Introduction

FastMCP is a Python framework for building **Model Context Protocol (MCP)** servers. An MCP server exposes tools, resources, prompts, and other components that AI assistants or MCP-compatible clients can use.

This guide walks through:

* Creating your first FastMCP server
* Adding tools
* Running the server
* Using the FastMCP CLI
* Connecting a client
* Creating visual UI tools

---

# Documentation Index

The complete FastMCP documentation index is available at:

```text
https://gofastmcp.com/llms.txt
```

Use this index to discover all available documentation pages before exploring the framework.

---

# Prerequisites

Before starting, install FastMCP by following the official installation instructions.

Once installed, you're ready to create your first MCP server.

---

# Creating Your First FastMCP Server

Every FastMCP application starts by creating a `FastMCP` instance.

Create a file named:

```text
my_server.py
```

Add the following code:

```python
from fastmcp import FastMCP

mcp = FastMCP("My MCP Server")
```

## Explanation

### Import FastMCP

```python
from fastmcp import FastMCP
```

Imports the `FastMCP` class.

---

### Create the Server

```python
mcp = FastMCP("My MCP Server")
```

Creates a new MCP server named:

```text
My MCP Server
```

At this stage the server exists but contains no tools.

---

# Adding Your First Tool

Tools are Python functions registered with the MCP server.

Use the `@mcp.tool` decorator.

Example:

```python
from fastmcp import FastMCP

mcp = FastMCP("My MCP Server")

@mcp.tool
def greet(name: str) -> str:
    return f"Hello, {name}!"
```

---

## How It Works

The decorator:

```python
@mcp.tool
```

registers the function as an MCP tool.

When an MCP client calls:

```text
greet
```

FastMCP executes:

```python
greet(name)
```

and returns:

```text
Hello, Ford!
```

---

# Running the Server

FastMCP supports multiple transports.

The two most common are:

* stdio
* HTTP

---

# Running with stdio

```python
from fastmcp import FastMCP

mcp = FastMCP("My MCP Server")

@mcp.tool
def greet(name: str) -> str:
    return f"Hello, {name}!"

if __name__ == "__main__":
    mcp.run()
```

Run:

```bash
python my_server.py
```

This starts the server using the default **stdio** transport.

---

# Running with HTTP

```python
from fastmcp import FastMCP

mcp = FastMCP("My MCP Server")

@mcp.tool
def greet(name: str) -> str:
    return f"Hello, {name}!"

if __name__ == "__main__":
    mcp.run(
        transport="http",
        port=8000
    )
```

Run:

```bash
python my_server.py
```

The server becomes available at:

```text
http://localhost:8000
```

---

# stdio vs HTTP

## stdio

Traditional MCP communication.

```text
Client
   │
stdin/stdout
   │
Server
```

Best for:

* Local integrations
* Desktop AI tools

---

## HTTP

Runs the server over HTTP.

```text
Client
   │
HTTP
   │
Server
```

Best for:

* Remote servers
* APIs
* Cloud deployment

---

# Why Use the **main** Block?

Example:

```python
if __name__ == "__main__":
    mcp.run()
```

This ensures:

* The server starts only when the file is executed directly.
* Compatibility with MCP clients that execute the server as a Python script.

If you always use the FastMCP CLI, this block is optional because the CLI imports the server object directly.

---

# Running with the FastMCP CLI

Instead of calling:

```python
mcp.run()
```

you can use the CLI.

---

## Run with stdio

```bash
fastmcp run my_server.py:mcp
```

---

## Run with HTTP

```bash
fastmcp run my_server.py:mcp --transport http --port 8000
```

### Important Note

The FastMCP CLI:

* Imports the `mcp` object
* Does **not** execute the `__main__` block

This means CLI options override any `mcp.run()` configuration in your file.

---

# Calling Your Server

Once the server is running over HTTP, connect to it using a FastMCP client.

Example:

```python
import asyncio
from fastmcp import Client

client = Client("http://localhost:8000/mcp")

async def call_tool(name: str):
    async with client:
        result = await client.call_tool(
            "greet",
            {"name": name}
        )
        print(result)

asyncio.run(call_tool("Ford"))
```

---

# Understanding the Client

Create the client:

```python
client = Client(
    "http://localhost:8000/mcp"
)
```

---

Enter the client context:

```python
async with client:
```

This establishes the connection.

---

Call a tool:

```python
await client.call_tool(
    "greet",
    {"name": name}
)
```

This invokes the server's `greet` tool.

---

Run the async function:

```python
asyncio.run(call_tool("Ford"))
```

Output:

```text
Hello, Ford!
```

---

# Why is asyncio Used?

FastMCP clients are asynchronous.

Instead of:

```python
call_tool()
```

you use:

```python
asyncio.run(call_tool())
```

to execute asynchronous code.

---

# Creating UI Tools

FastMCP tools normally return text.

However, tools can also return interactive visual interfaces.

This requires:

```bash
pip install "fastmcp[apps]"
```

---

# Enabling App Tools

Use:

```python
@mcp.tool(app=True)
```

instead of:

```python
@mcp.tool
```

The `app=True` option tells FastMCP that the tool returns a visual component rather than plain text.

---

# Example UI Tool

```python
from prefab_ui.app import PrefabApp
from prefab_ui.components import (
    Column,
    Heading,
    Text,
    Badge,
    Row
)

from fastmcp import FastMCP

mcp = FastMCP("My MCP Server")

@mcp.tool(app=True)
def greet(name: str) -> PrefabApp:

    with Column(gap=4, css_class="p-6") as view:

        Heading(f"Hello, {name}!")

        with Row(gap=2, align="center"):

            Text("Status")

            Badge(
                "Greeted",
                variant="success"
            )

    return PrefabApp(view=view)
```

---

# What Does app=True Do?

When using:

```python
@mcp.tool(app=True)
```

FastMCP automatically:

* Registers the tool
* Adds rendering metadata
* Returns UI components instead of plain text

The MCP host renders:

* Cards
* Tables
* Charts
* Forms
* Dashboards
* Other visual components

---

# Previewing UI Tools

You can preview app tools locally without an MCP host.

Run:

```bash
fastmcp dev apps my_server.py
```

This launches a local development environment for visual tools.

---

# Prefab UI Components Used

The example uses:

* `Column`
* `Row`
* `Heading`
* `Text`
* `Badge`
* `PrefabApp`

These components build the visual interface returned by the tool.

---

# Quick Workflow

```text
Create FastMCP Server
        │
        ▼
Register Tools
        │
        ▼
Run Server
        │
        ▼
Connect Client
        │
        ▼
Call Tool
        │
        ▼
Receive Response
```

---

# Summary

FastMCP allows you to:

* Create MCP servers
* Register Python functions as tools
* Run servers using stdio or HTTP
* Connect clients asynchronously
* Build interactive UI tools using Prefab
* Preview visual tools locally
* Launch servers through Python or the FastMCP CLI

This Quickstart demonstrates the complete workflow from creating a server to exposing tools that can be called by MCP-compatible clients.
