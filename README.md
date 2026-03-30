**Summary**:

This is a AI Test Agent Project (Draft Stage) which has been developed using Google ADK in Multi Agent Architecture.
As of now, if we give a prompt "Fetch userstories from CRED project which are in Ready for test state, prepare, classify, execute and report them"
Agent works as follows
1. jira_fetcher agent fetches jira userstories
2. test_designer creates test cases of that userstory
3. test_classifier classifies testcases as UI or API
4. ui_execution will execute ui testcases and report summary in console
   
**Pre-Requisite**:

1. Added you in my jira project account as admin, you might have received in your provided personal emails, please check

**How to Setup**:

1. install python version 3.11.9
2. install pycharm community version
3. clone the repo
4. Open any terminal
5. cd Test-Agent
6. create virutal environment with command python3 -m venv .venv
7. activate virtual environment as per your terminal

<img width="797" height="812" alt="image" src="https://github.com/user-attachments/assets/fa6c5c04-6c75-408e-99d9-697df9277c45" />

8. once activate your terminal will look like .venv will appear the prefix of the terminal
   
<img width="425" height="64" alt="image" src="https://github.com/user-attachments/assets/6dbb8788-662c-444a-b0fa-9f56cd4e85ef" />

9. Now, install google adk using "pip install google-adk" in your .venv

10. inorder to use jira mcpserver, install uv using "pip install uv" in your .venv

11. inroder to use playwright mcp, we need to install node.js using installer in your machine
   
12. As this is still a draft project, there is still no main.py created, so please run "adk web" or "adk run orchestrator" to see how agent works

**How to configure .env**:

1. create .env at root level

<img width="591" height="492" alt="image" src="https://github.com/user-attachments/assets/3664f581-0506-4f91-aa91-18c5067449cf" />

2. If you want to use vertex AI, create google cloud account and create project inside that account with active billing or free credit
3. run "gcloud auth application-default login" in command prompt terminal which generates application_default_credentials.json
4. run "gcloud config set project [YOUR-PROJECT-ID]"
5. keep below keys in .env file

GOOGLE_GENAI_USE_VERTEXAI=1

GOOGLE_CLOUD_PROJECT=[YOUR-PROJECT-ID]

GOOGLE_CLOUD_LOCATION="us-central1"

CLOUDSDK_CORE_PROJECT=[YOUR-PROJECT-ID]

GOOGLE_APPLICATION_CREDENTIALS=location generated from gcloud auth application-default login for application_default_credentials.json

JIRA_URL=https://gurumeharadivi.atlassian.net/

JIRA_USERNAME="your email id in above url"

JIRA_API_TOKEN="your jira api token of above url"

6. steps 2, 3, 4 are not present if you want to use GOOGLE API backend instead of VERTEX API
