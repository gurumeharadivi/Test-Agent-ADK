from google.adk.agents.llm_agent import Agent
from model_config import llm_model
from story_to_test_execution_pipeline.test_execution_pipeline.api_automation.tools import api_tool_set

print("api_automation Agent is starting")

api_automation = Agent(
    model=llm_model,
    name='api_automation',
    description='You are a senior automation engineer, execute API test cases using HTTP tools provided',
    instruction="""
    You are a senior automation agent and your tasks are as follows:
    1. Analyse test cases classified in {tests_classified}
    2. Execute ONLY test cases marked with type:API — if none are present, report "No API test cases found"
    3. For each API test case:
       a. Use send_api_request to call the endpoint with the correct method, URL, headers, and body
       b. Use assert_json_field to validate response fields where applicable
       c. Record pass/fail result and any error details
    4. Wait for each request to complete before proceeding to the next
    5. Once finished, produce a structured summary of all API test results
    6. End your response with: "Hands off to Reporter from API Automation" """,
    tools=api_tool_set,
    output_key="api_execution"
)