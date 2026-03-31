from google.adk.agents.llm_agent import Agent
from model_config import llm_model
from story_to_test_execution_pipeline.test_execution_pipeline.ui_automation.tools import playwright_tool_set

print("ui_automation Agent is starting")

ui_automation = Agent(
    model=llm_model,
    name='ui_automation',
    description='You are an senior automation engineer, create ui automation scripts and execute using tools provided',
    instruction="""
    You are a senior automation agent and Your tasks are as follow
    1. Analyse testcases classified in generated {tests_classified}
    2. Execute only the ones with type:UI and execute only UI Test cases if present else no need to execute
    3. create ui automation scripts for them using tools provided
    4. Execute those scripts with headless mode as off
    5. close any browser popups
    6. wait properly for the element to load avoid element not found exceptions
    7. Retry if any issue occurs due to malfunction of application
    8. Monitor the tool execution and report accordingly with test results total tests executed
    9. Once finished, End your Conversation with Hands off to Reporter from UI Automation""",
    tools=[playwright_tool_set],
    output_key="ui_execution"
)