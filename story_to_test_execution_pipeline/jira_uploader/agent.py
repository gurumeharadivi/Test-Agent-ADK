from google.adk.agents.llm_agent import Agent

from story_to_test_execution_pipeline.prep_pipeline.jira_fetcher.tools import jira_tool_set

print("Jira tools retrieved from MCP Server")

jira_uploader = Agent(
    name='jira_uploader',
    description='you are a jira uploader. You will create test cases and defects ',
    instruction="""
    You are a JIRA Uploader and your task is as follows
    - input the result from TestExecutionAgent agent output 'test_execution'
    - Upload test cases by filling all the mandatory fields
    - fill the details of the test case in meaning ful way
    - Execute them as per the input
    - Upload attachments for pass or fail
    - Create defects by filling mandatory fields for failed test cases
    - prepare replication steps, expected and actual output clearly
    - upload respective failure screenshot captured
    - Comment Detailed Summary in Respective Userstory
    """,
    tools=[jira_tool_set],
    output_key="testcases_defects_upload"
)