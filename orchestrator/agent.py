from google.adk.agents import LlmAgent
import os
from google.adk.models.google_llm import Gemini
from prep_pipeline.agent import prep_pipeline
from ui_automation.agent import ui_automation
from reporter.agent import reporter
print("Orchestrator Agent")

# Initialize the model via Vertex AI
llm_model = Gemini(
    model_name="gemini-2.5-flash"
    # ADK uses your project ID from the environment
)
test_orchestrator = LlmAgent(
    #model=os.getenv("MODEL"),
    model=llm_model,
    name='test_orchestrator',
    description='You are Lead QA Manager, Monitor the process and retry if necessary',
    instruction="""
    You are the Lead QA Manager.
    1. Use prep_pipeline, ui_automation, reporter effectively to complete the tasks.
    2. Monitor shared session state for completion.
    3. If a tool fails in the ui_automation, attempt one retry.
    4. Ensure final_report contains a 1:1 match of stories to results.
    """,
    sub_agents=[prep_pipeline,ui_automation,reporter]
)
root_agent = test_orchestrator