import os

from dotenv import load_dotenv
from google.adk.agents import LlmAgent
from google.adk.models.google_llm import Gemini
from google.genai.types import HttpRetryOptions

from story_to_test_execution_pipeline.agent import story_to_test_execution_pipeline
load_dotenv()
print("Orchestrator Agent")


# Verify it loaded (remove after testing)
print("OPENAI KEY LOADED:", os.getenv("OPENAI_API_KEY") is not None)
#story_to_execution_agent_tool = AgentTool(agent = story_to_test_execution_pipeline)
# Define the structured options
retry_config = HttpRetryOptions(
    attempts=5,
    initial_delay=2.0,
    max_delay=60.0,
    # Note: Check if your version uses 'multiplier' or 'backoff_factor'
    # If 'multiplier' failed before, stick to these three core keys.
)
llm_model = Gemini(
        model=os.getenv("GEMINI_MODEL"),
        retry_options=retry_config # Pass the object, not a dict
)

root_agent = LlmAgent(
    #model=os.getenv("MODEL"),
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