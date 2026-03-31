from google.adk.agents.llm_agent import Agent
from model_config import llm_model
from story_to_test_execution_pipeline.prep_pipeline.jira_fetcher.tools import jira_tool_set

print("Jira tools retrieved from MCP Server")

jira_fetcher = Agent(
    model=llm_model,
    name='jira_fetcher',
    description='you are a jira fetcher ',
    instruction="""You have to connect to JIRA and get the user stories in Ready For Test Status using jira_tool_set
    USE  JQL Query project = CRED AND type = Story AND status = "Ready For Test" ORDER BY created DESC
    End your Conversation with Hands off to Test Designer Agent""",
    tools=[jira_tool_set],
    output_key="raw_stories"
)