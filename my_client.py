from logger import logger
import asyncio
from fastmcp import Client
from contextlib import AsyncExitStack


client = Client("http://localhost:8000/mcp")

async def call_tool(name: str):
    logger.info(f"Client initiating call to tool: greet with name: {name}")
    async with client:
        result = await client.call_tool("greet", {"name": name})
        logger.info(f"Client received response: {result}")
        print(result)


if __name__ == "__main__":
    asyncio.run(call_tool("Dhiraj"))

