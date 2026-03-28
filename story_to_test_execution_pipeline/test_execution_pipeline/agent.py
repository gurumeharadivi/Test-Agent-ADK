from google.adk.agents import ParallelAgent

from story_to_test_execution_pipeline.test_execution_pipeline.api_automation.agent import api_automation
from story_to_test_execution_pipeline.test_execution_pipeline.ui_automation.agent import ui_automation

print("Parallel Binding Execution Agents")

test_execution_pipeline = ParallelAgent(
    name="test_execution_pipeline",
    description="""Your a parallel workflow agent, {tests_classified} is given as input
                     All UI Tests should go to ui_automation
                    ALL API Test should go to api_automation""",
    sub_agents=[ui_automation,api_automation],
)