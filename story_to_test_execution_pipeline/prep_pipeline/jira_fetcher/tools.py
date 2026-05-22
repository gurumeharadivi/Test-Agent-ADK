import os

from dotenv import load_dotenv
from google.adk.tools.mcp_tool import McpToolset, StdioConnectionParams
from mcp import StdioServerParameters
load_dotenv()
print("Connecting to JIRA MCP Server from Jira_fetcher")

jira_tool_set = McpToolset(
    connection_params=StdioConnectionParams(
        server_params=StdioServerParameters(
        command="uvx",
        args=["mcp-atlassian"],
        env={
        "JIRA_URL": os.getenv("JIRA_URL"),
        "JIRA_USERNAME": os.getenv("JIRA_USERNAME"),
        "JIRA_API_TOKEN": os.getenv("JIRA_API_TOKEN")
        }

        ),
        timeout=600
    )
)
print("got the jira tools from MCP")