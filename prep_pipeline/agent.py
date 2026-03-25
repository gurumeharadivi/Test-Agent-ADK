from google.adk.agents import SequentialAgent

from test_classifier.agent import test_classifier
from jira_fetcher.agent import jira_fetcher
from test_designer.agent import test_designer

print("Binding Processing Agents")

prep_pipeline = SequentialAgent(
    name="prep_pipeline",
    description="End to End pipeline from fetching jira userstores, creation and classification of test cases",
    sub_agents=[jira_fetcher,test_designer,test_classifier]
)