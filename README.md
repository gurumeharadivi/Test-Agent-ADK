Summary:

This is a AI Test Agent Project (Draft Stage) which has been developed using Google ADK in Multi Agent Architecture. As of now, if we give a prompt "Fetch userstories from CRED project which are in Ready for test state, prepare, classify, execute and report them" Agent works as follows

jira_fetcher agent fetches jira userstories
test_cases_designer agent designes test cases
test_execution_agent will execute testcases and report summary in json format in console
Pre-Requisite:

Added you in my jira project account as admin, you might have received in your provided personal emails, please check
How to Setup:

install python version 3.11.9
install pycharm community version
clone the repo
Open any terminal
cd Test-Agent
create virutal environment with command python3 -m venv .venv
activate virtual environment as per your terminal
image
once activate your terminal will look like .venv will appear the prefix of the terminal
image
Now, install google adk using "pip install google-adk" in your .venv

inorder to use jira mcpserver, install uv using "pip install uv" in your .venv

inroder to use playwright mcp, we need to install node.js using installer in your machine

As this is still a draft project, there is still no main.py created, so please run "adk web" or "adk run orchestrator" to see how agent works

How to configure .env:

create .env at root level
image
If you want to use vertex AI, create google cloud account and create project inside that account with active billing or free credit
run "gcloud auth application-default login" in command prompt terminal which generates application_default_credentials.json
run "gcloud config set project [YOUR-PROJECT-ID]"
keep below keys in .env file
GOOGLE_GENAI_USE_VERTEXAI=1

GOOGLE_CLOUD_PROJECT=[YOUR-PROJECT-ID]

GOOGLE_CLOUD_LOCATION="global"

CLOUDSDK_CORE_PROJECT=[YOUR-PROJECT-ID]

GOOGLE_APPLICATION_CREDENTIALS=location generated from gcloud auth application-default login for application_default_credentials.json

JIRA_URL=https://gurumeharadivi.atlassian.net/

JIRA_USERNAME="your email id in above url"

JIRA_API_TOKEN="your jira api token of above url"
OPENAI_API_KEY=""your open ai api token"
USER="Your Name"
GEMINI_MODEL=gemini-3.5-flash
OPENAI_MODEL=openai/gpt-5

steps 2, 3, 4 are not present if you want to use GOOGLE API backend instead of VERTEX API
