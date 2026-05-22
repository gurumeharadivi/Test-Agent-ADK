from google.adk.agents import LlmAgent, LoopAgent, SequentialAgent
from google.adk.agents.callback_context import CallbackContext
from google.adk.tools import ToolContext

# --- State Keys ---
STATE_CURRENT_TESTS = "current_testcases"
STATE_CRITICISM = "criticism"
# Define the exact phrase the Critic should use to signal completion
COMPLETION_PHRASE = "No major issues found."

# --- Tool Definition ---
def exit_loop(tool_context: ToolContext):
    """Call this function ONLY when the critique indicates no further changes are needed, signaling the iterative process should end.
    Returns the finalized test cases to the next agent."""
    print(f"  [Tool Call] exit_loop triggered by {tool_context.agent_name}")
    
    # Extract the finalized test cases from state to pass to next agent
    finalized_test_cases = tool_context.state.get(STATE_CURRENT_TESTS, "")

    # Ensure the finalized test cases are explicitly written back into the session state
    tool_context.state[STATE_CURRENT_TESTS] = finalized_test_cases

    # Signal the loop to exit and skip additional summarization
    tool_context.actions.escalate = True
    tool_context.actions.skip_summarization = True

    # Return the finalized test cases so any caller gets them as well
    return {
        "status": "completed",
        "finalized_test_cases": finalized_test_cases,
        "message": "Test case refinement completed successfully. Loop exited."
    }

# --- Before Agent Callback ---
def update_initial_topic_state(callback_context: CallbackContext):
    """Ensure 'initial_topic'  set in state before pipeline starts."""
    callback_context.state['initial_topic'] = callback_context.state.get('initial_topic', 'test cases should be generated from user stories present in {raw_stories} fetched by jira fetcher agent')

# --- Agent Definitions ---

# STEP 1: Initial Writer Agent (Runs ONCE at the beginning)
initial_test_cases_designer_agent = LlmAgent(
    name="InitialTestDesignerAgent",
    include_contents='none',
    instruction=f"""
    You are a Creative Test Designer Assistant tasked with creation of test cases.
    Write a *high level* first draft of a testcases
    Keep it plain and minimal - do NOT add detailed test cases yet.
    Output *only* test cases, Do Not add detailed test steps
    """,
    description="Writes the initial high level testcases based on user story, aiming for some initial substance.",
    output_key=STATE_CURRENT_TESTS
)

# STEP 2a: Critic Agent (Inside the Refinement Loop)
critic_agent_in_loop = LlmAgent(
    name="CriticAgent",
    include_contents='none',
    instruction=f"""
    You are a Constructive Critic AI reviewing test cases draft.

    **TestCases to Review:**
    ```
    {{current_testcases}}
    ```

    **Completion Criteria (ALL must be met):**
   Your tasks:
    1. Review each test case for adherence to ISTQB Standards:
       - Equivalence Class Partitioning: Ensure valid and invalid partitions are covered
       - Boundary Value Analysis: Check for boundary conditions (min, max, just inside/outside boundaries)
       - Positive Testing: Verify happy path scenarios
       - Negative Testing: Ensure error conditions, invalid inputs, and failure scenarios are tested
       - State Transition Testing: If applicable, check state changes
       - Use Case Testing: Cover all paths in user stories
       - Decision Table Testing: For complex logic with multiple conditions
       - Pairwise Testing: For combinations, if applicable
       - Create Sanity Test Case with Scope of only Login with username and password and page loaded successfully

    2. Assess completeness:
       - Are all user story requirements covered?
       - Are there missing test scenarios for edge cases, error handling, security, performance?
       - Is test data appropriate and deterministic?
       - Are steps clear, precise, and executable?
       - Do expected results align with requirements?

    3. Identify any gaps or issues:
       - List specific missing scenarios
       - Point out incorrect or incomplete test cases
       - Suggest improvements for better coverage
    4. Application under test details like url, username, password is as per the data in {{raw_stories}}
    5. Other details like field inputs can be manufactured if necessary
    6. Ensure Generated Test cases should be with in scope of Userstory
    7. Observe and criticise possible test cases can be combined in a single test case if can be executed in single flow
 **Task:**
    Check the testcases against the criteria above.

    IF any criteria is NOT met, provide specific feedback on what to add or improve.
    Output *only* the critique text.
    **IMPORTANT**
    IF Only ALL criteria are met, respond *exactly* with: "{COMPLETION_PHRASE}"
    """,
    description="Reviews the current testcases, providing critique if clear improvements are needed, otherwise signals completion.",
    output_key=STATE_CRITICISM
)

# STEP 2b: Refiner/Exiter Agent (Inside the Refinement Loop)
refiner_agent_in_loop = LlmAgent(
    name="RefinerAgent",
    include_contents='none',
    instruction=f"""
    You are a Creative Testcases Designer Assistant refining test cases based on feedback OR exiting the process.
    **Current TestCases:**
    ```
    {{current_testcases}}
    ```
    **Critique/Suggestions:**
    {{criticism}}

    **Task:**
    Analyze the 'Critique/Suggestions'.
    IF the critique is *exactly* "{COMPLETION_PHRASE}":
        Call the exit_loop tool to exit the refinement loop. Do not output any text.
    ELSE (the critique contains actionable feedback):
        Carefully apply the suggestions to improve the 'Current TestCases'. Output *only* the refined test cases.
    test cases should be of in JSON with below format
     *Example of UI TestCase*
     UserStory: APAC-001 (JIRA KEY Fetched from {{raw_stories}})
     Test Type: UI,
     TestcaseId: TC01 (TestcaseId should follow sequential order TC01 TC02 TC03 ....TC15)
     Title: Verify login of application,
     Description: Login of Application with Username and password,
     Test Steps:
     1. Open the respective Application url present in user story
     2. input username
     3. input password
     4. Click Login
     5. Ensure Login is successful
     Expected Result:
     Once Login, Home page should be loaded successfully
     *Example of API TestCase*
     UserStory: APAC-001 (JIRA KEY Fetched from {{raw_stories}})
     Test Type: API,
     TestcaseId: TC01,
     Title: Verify End to End working  of the Service is fine,
     Description: Methods defined for the service should be working fine,
     Test Steps:
     1. Call POST Endpoint with given headers request body
     2. Ensure to get 201 created response
     3. call Get Endpoint with given headers and take required data generated in POST Response as Input
     4. Ensure to get 200 ok response
     5. call PUT Endpoint with given headers and take required data generated in POST Response as Input
     6. Ensure to get 204 response
     7. call Get Endpoint with given headers and take required data generated in POST Response as Input
     8. Ensure Status that was updated using PUT Endpoint is fetched
     Expected Result:
     1. Ensure status fetched in step 3 should be same as created by POST
     2. Ensure status fetched in step 8 should be same as updated by PUT
     ***
    Include One Sanity test case of the application and keep the title as Sanity as per your understanding of the user story
    CRITICAL:
    USE Your *Intelligence* in combining test cases that can be executed in single workflow
    STRICTLY Do not create test cases which are not scope of the user story.
    DO NOT MANUFACTURE URL or End Points for testcase preparation
    for the data which is not present in user story manufacture it accordingly
    """,
    description="Refines the created test cases based on critique, or exit the loop if critique indicates completion.",
    tools=[exit_loop],
    output_key=STATE_CURRENT_TESTS
)

# STEP 2: Refinement Loop Agent
refinement_loop = LoopAgent(
    name="RefinementLoop",
    # Agent order is crucial: Critique first, then Refine/Exit
    sub_agents=[
        critic_agent_in_loop,
        refiner_agent_in_loop,
    ],
    max_iterations=5 # Limit loops
)

# STEP 3: Overall Sequential Pipeline
# For ADK tools compatibility, the root agent must be named `root_agent`
test_cases_creation_agent = SequentialAgent(
    name="IterativeTestDesignerPipeline",
    sub_agents=[
        initial_test_cases_designer_agent, # Run first to create initial doc
        refinement_loop       # Then run the critique/refine loop
    ],
    before_agent_callback=update_initial_topic_state, # set initial topic in state
    description="Writes an initial test cases and then iteratively refines it with critique"
)
