from google.adk.agents.llm_agent import Agent

from story_to_test_execution_pipeline.test_execution_pipeline.ui_automation.tools import playwright_tool_set

print("api_automation Agent is starting")

api_automation = Agent(
    name='api_automation',
    description='You are an senior automation engineer, create api automation scripts and execute using tools provided',
    instruction="""
    You are a senior automation agent and Your tasks are as follow
    1. Analyse testcases classified in generated {tests_classified}
    2. Execute testcases which are marked with type:API only if present else do not execute
    3. create api automation scripts for them using tools provided
    6. wait properly for the request to complete
    7. Once finished, End your Conversation with Hands off to Reporter from API Automation """,
    tools=[playwright_tool_set],
    output_key="api_execution"
)