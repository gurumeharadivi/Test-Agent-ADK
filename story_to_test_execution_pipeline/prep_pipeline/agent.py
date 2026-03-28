from google.adk.agents import SequentialAgent

from story_to_test_execution_pipeline.prep_pipeline.jira_fetcher.agent import jira_fetcher
from story_to_test_execution_pipeline.prep_pipeline.test_classifier.agent import test_classifier
from story_to_test_execution_pipeline.prep_pipeline.test_designer.agent import test_designer

print("Binding Processing Agents")

prep_pipeline = SequentialAgent(
    name="prep_pipeline",
    description="End to End pipeline from fetching jira user stories, creation and classification of test cases",
    sub_agents=[jira_fetcher,test_designer,test_classifier]
)