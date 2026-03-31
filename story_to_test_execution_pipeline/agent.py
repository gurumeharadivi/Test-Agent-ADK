from google.adk.agents import SequentialAgent

from story_to_test_execution_pipeline.prep_pipeline.agent import prep_pipeline
from story_to_test_execution_pipeline.reporter.agent import reporter
from story_to_test_execution_pipeline.test_execution_pipeline.agent import test_execution_pipeline

print("Binding preparation pipeline, execution pipeline, and reporter")

story_to_test_execution_pipeline = SequentialAgent(
    name="story_to_test_execution_pipeline",
    description="End to End pipeline from fetching jira userstories, creation, classification, execution and reporting of test cases",
    sub_agents=[prep_pipeline, test_execution_pipeline, reporter]
)
root_agent = story_to_test_execution_pipeline