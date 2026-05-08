from google.adk.agents import SequentialAgent

from story_to_test_execution_pipeline.execution_orchestrator_agent.agent import test_execution_agent
from story_to_test_execution_pipeline.prep_pipeline.agent import prep_pipeline

print("Binding preparation of testcase pipeline execution pipeline and reporter")

story_to_test_execution_pipeline = SequentialAgent(
    name="story_to_test_execution_pipeline",
    description="End to End pipeline from fetching jira userstories, creation, classification, execution of test cases",
    sub_agents=[prep_pipeline, test_execution_agent]
)