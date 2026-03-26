from google.adk.agents.llm_agent import Agent
from ui_automation.tools import playwright_tool_set
print("Reporter Agent is starting")

reporter = Agent(
    name='reporter',
    description='You are a QA Lead, who tracks the execution of test cases either ui or api and create a report',
    instruction="""
    You are a QA Lead
    Your tasks are as follow
    1. Monitor ui_automation agent
    2. Analyse generated {ui_execution}
    3. create a beautiful html report
    """,
    tools=[playwright_tool_set],
    output_key="final_report"
)