from google.adk.agents.llm_agent import Agent

print("Reporter Agent is starting")

reporter = Agent(
    name='reporter',
    description='You are a QA Lead, who tracks the execution of test cases either ui or api and create a report',
    # instruction="""
    # You are a QA Lead
    # Your tasks are as follow
    # 1. Ensure total testcases designed in {test_designer} are same as {tests_classified} if data present, else report as No data present in desginer and classifer
    # 2. Ensure total testcases in {tests_classified } are executed in {ui_execution} {api_execution} if data present, else report as No data present in Execution
    # 3. If total test cases are not present get the status from respective agent and report
    # 4. create clean Mark UP Report
    # """,
instruction="""
    You are a QA Lead
    Your tasks are as follow
    1. Analyze results present in {ui_execution} {api_execution} if data present, else report as No data present in Execution
    create clean Mark UP Report
    """,
    output_key="final_report"
)