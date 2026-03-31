from google.adk.agents.llm_agent import Agent
from model_config import llm_model

print("Test Classifier Agent is starting")

test_classifier = Agent(
    model=llm_model,
    name='test_classifier',
    description='you are a senior qe engineer who classifies test cases after reading test cases',
    instruction="""
    Analyze the generated test cases: {test_cases}
    Categorize each test case into one of two categories:
    - 'UI': If the test requires browser interaction (Playwright/Selenium).
    - 'API': If the test can be verified via REST endpoints.
    Return the list of test cases with a new 'type' field added to each.
    End your Conversation with Hands off to ui_automation
    """,
    output_key="tests_classified"
)