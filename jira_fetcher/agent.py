from google.adk.agents.llm_agent import Agent
import os

from jira_fetcher.tools import jira_tool_set

print("Jira tools retrieved from MCP Server")
# jira_fetcher = Agent(
#     model=os.getenv("MODEL"),
#     name='jira_fetcher',
#     description='you are a jira fetcher ',
#     instruction="""You have to connect to JIRA and get the user stories in Ready For Test Status using jira_tool_set
#     USE  JQL Query project = CRED AND type = Story AND status = "Ready For Test" ORDER BY created DESC
#     End your Conversation with Hands off to Test Designer Agent""",
#     tools=[jira_tool_set],
#     output_key="raw_stories"
# )
jira_fetcher = Agent(
    name='jira_fetcher',
    description='you are a jira fetcher ',
    instruction="""You have to connect to JIRA and get the user stories in Ready For Test Status using jira_tool_set
    USE  JQL Query project = CRED AND type = Story AND status = "Ready For Test" ORDER BY created DESC
    End your Conversation with Hands off to Test Designer Agent""",
    tools=[jira_tool_set],
    output_key="raw_stories"
)