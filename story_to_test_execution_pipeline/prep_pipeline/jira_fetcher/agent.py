from google.adk.agents.llm_agent import Agent

from story_to_test_execution_pipeline.prep_pipeline.jira_fetcher.tools import jira_tool_set

print("Jira tools retrieved from MCP Server")

jira_fetcher = Agent(
    name='jira_fetcher',
    description='you are a jira fetcher ',
    instruction="""
    You are a JIRA Agent and your task is as follows
    - GET the user stories in Ready For Test Status using jira_tool_set
    - USE  JQL Query: project = CRED AND type = Story AND status = "Ready For Test" ORDER BY created DESC for faster filtering
    """,
    tools=[jira_tool_set],
    output_key="raw_stories"
)