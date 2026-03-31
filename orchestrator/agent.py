from dotenv import load_dotenv
from google.adk.agents import LlmAgent
from model_config import llm_model
from story_to_test_execution_pipeline.agent import story_to_test_execution_pipeline
load_dotenv()
print("Orchestrator Agent")

root_agent = LlmAgent(
    model=llm_model,
    name='test_orchestrator',
    description='You are Lead QA Manager, Monitor the process and retry if necessary',
    instruction="""
    You are the Lead QA Manager.
    Understand the user prompt and them trigger the respective pipeline
    story_to_execution_agent_tool - This tool is used to fetch user stories from JIRA, create test cases, execute them and prepare report
    Once the task is complete, Show the Summary Results
    """,
    sub_agents = [story_to_test_execution_pipeline]
)