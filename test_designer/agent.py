from google.adk.agents.llm_agent import Agent
import os

print("Test Desginer Agent is starting")

test_designer = Agent(
    #model=os.getenv("MODEL"),
    name='test_designer',
    description='you are a senior qe engineer who designs test cases after reading user stories',
    instruction="""
    You are a Senior QA Automation Engineer.
    Input: A list of User Stories from Jira: {raw_stories}
    Note: Manufacture test data if necessary
    Task: For each story, generate detailed test cases using test design techniques including:
    1. Test Case ID
    2. Description
    3. Test Data
    4. Step-by-step actions
    5. Expected Result
    Output: Provide the result in a structured JSON-like list format.
    End your Conversation with Hands off to Test Classifier Agent
    """,
    output_key="test_cases"
)