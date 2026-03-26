from google.adk.agents.llm_agent import Agent
from ui_automation.tools import playwright_tool_set
print("ui_automation Agent is starting")

ui_automation = Agent(
    name='ui_automation',
    description='You are an senior automation engineer, create automation scripts and executing using tools',
    instruction="""
    You are a senior automation agent and Your tasks are as follow
    1. Analyse generated {classified_tasks}
    2. Pick the one that marked with type:UI
    3. create automation scripts for them using tools provided
    4. Execute those scripts with headless mode as off
    5. If found issues, correct accordingly as per the UI application you access
    6. wait properly for the element to avoid element not found exceptions""",
    tools=[playwright_tool_set],
    output_key="ui_execution"
)