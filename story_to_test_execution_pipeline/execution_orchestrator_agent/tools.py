import json
from typing import Any, Dict, List
from datetime import datetime

from dotenv import load_dotenv
from google.adk.tools.mcp_tool import McpToolset, StdioConnectionParams
from google.adk.tools import BaseTool
from mcp import StdioServerParameters

load_dotenv()
print("Connecting to Playwright MCP Server for execution_orchestrator_agent agent")

playwright_tool_set = McpToolset(
    connection_params=StdioConnectionParams(
        server_params=StdioServerParameters(
        command="npx",
        args= [
        "@playwright/mcp@latest"
      ]
        ),
        timeout=600
    )
)

file_server_tool_set = McpToolset(
connection_params=StdioConnectionParams(
        server_params=StdioServerParameters(
        command="npx",
        args= [
        "-y",
        "@modelcontextprotocol/server-filesystem",
        "C:/Users/mehar/Test-Agent/reports"
      ]
        ),
        timeout=600
    )

)
print("got the tools from MCP")