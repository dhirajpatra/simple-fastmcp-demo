# Simple MCP Server and Client Demo from FastMCP

This is just followed the demo from FastMCP. However adding few tips to run in your local system may helpful.

## Steps

* install FastMCP
* Run `pip install -r requiremetns.txt`
* Update or create the .env file with ANTHROPIC_API_KEY=your-api-key-goes-here
* run server by `fastmcp run my_server.py:mcp --transport http --port 8000` or `python my_server.py` in one terminal
* run client by `python my_client.py` in another terminal


If you try to run server by `python my_server.py` it will start in the server starts using stdio (Standard Input/Output). In this case you can't run client by `python my_client.py` because it will not able to find the server.


## Information

The Communication Flow:

User/LLM Request: The LLM decides it needs a tool (e.g., "Check the weather" or "Query a database").

Client Call: Your Client (my_client.py) receives this request and calls the specific tool on the MCP Server.

Server Execution: The MCP Server runs the local code, fetches the data, and sends the result back to the Client.

Client Forwarding: The Client takes that raw data and sends it to the LLM as context.

Final Output: The LLM uses that context to give you a human-readable answer.

Key Distinction:

The Server never talks to the LLM directly. It is "blind" to the LLM.

The Client (your app) manages the security, the connection, and the conversation flow.

## Continue develop this application in future

Thanks for your support