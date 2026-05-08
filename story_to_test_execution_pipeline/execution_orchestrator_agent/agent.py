import os

from google.adk import Agent
from google.adk.agents import LlmAgent
from google.adk.models import LiteLlm
from google.adk.tools import AgentTool

from story_to_test_execution_pipeline.execution_orchestrator_agent.tools import playwright_tool_set, file_server_tool_set

# Test Execution Agent - executes test cases with playwright tools
test_execution_agent = Agent(
    name="TestExecutionAgent",
    model=LiteLlm(
        model=os.getenv("OPENAI_MODEL"),
        api_key=os.getenv("OPENAI_API_KEY")),
    description="You are a Test Execution Agent who executes testcases with the tools provided",
    instruction="""
    Short instructions for TestExecutionAgent (concise to reduce prompt size):
    - Input: a prepared context variable `finalized_test_cases` (list/dict of testcases) and `user_story` id.
    - Responsibility: execute each testcase using the provided tools (playwright_tool_set and file_server_tool_set).
    - For UI tests: run with headless mode OFF, start a fresh browser per testcase and clear cache before each testcase.
    - Save artifacts: create a folder named 'TestCaseId - Title' and save a screenshot per step by marking the field on which test execution is performed.
    - Do NOT perform orchestration, test case design, or loop control. Expect `current_testcases` to be ready.
    - Do Not Stop the execution if test case failed, continue with other testcases by marking the failed one as FAIl
    Output (exact machine-readable JSON) under key `test_execution` with this schema:
    {"user_story": "<id>", "summary": {"total":int,"passed":int,"failed":int,"skipped":int}, "results": [{"testcase_id":"TC01","title":"...","status":"PASS|FAIL|SKIP","failure_step":"","failure_reason":"","expected":"","actual":""}]}

    Rules:
    - Every testcase in `current_testcases` must appear exactly once in `results`.
    - For FAIL fill `failure_step` and `failure_reason` precisely.
    - Keep values machine-parsable (short strings, no paragraphs).
    """,
    tools=[playwright_tool_set,file_server_tool_set],
    output_key="test_execution"
)

