import os

from dotenv import load_dotenv
from google.adk.tools.mcp_tool import McpToolset, StdioConnectionParams
from mcp import StdioServerParameters
load_dotenv()
print("Connecting to Playwright MCP Server for ui_automation agent")

playwright_tool_set = McpToolset(
    connection_params=StdioConnectionParams(
        server_params=StdioServerParameters(
        command="npx",
        args= [
        "@playwright/mcp@latest"
      ]
        ),
        timeout=300
    )
)
print("got the tools from MCP")