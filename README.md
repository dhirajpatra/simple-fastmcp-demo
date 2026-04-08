# Simple MCP Server and Client Demo from FastMCP

This is just followed the demo from FastMCP. However adding few tips to run in your local system may helpful.

## Steps

1. install FastMCP
2. run server by `fastmcp run my_server.py:mcp --transport http --port 8000` 
3. run client by `python my_client.py`


If you try to run server by `python my_server.py` it will start in the server starts using stdio (Standard Input/Output). In this case you can't run client by `python my_client.py` because it will not able to find the server.

## Continue develop this application in future

Thanks for your support