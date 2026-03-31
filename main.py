"""Entry point for the Test-Agent ADK application.

Usage:
    python main.py                         # Interactive mode (default prompt)
    python main.py --project MYPROJECT     # Run for a specific Jira project key
    python main.py --status "In Progress"  # Override the Jira story status filter
    python main.py --web                   # Launch ADK web UI instead
"""

import argparse
import asyncio

from dotenv import load_dotenv

load_dotenv()


def build_prompt(project: str, status: str) -> str:
    return (
        f'Fetch user stories from {project} project which are in "{status}" state, '
        f"prepare test cases, classify them, execute them, and generate a report."
    )


async def run_agent(prompt: str) -> None:
    from google.adk.runners import Runner
    from google.adk.sessions import InMemorySessionService
    from google.genai.types import Content, Part

    from orchestrator.agent import root_agent

    session_service = InMemorySessionService()
    session = await session_service.create_session(
        app_name="test_agent", user_id="user", session_id="session-1"
    )

    runner = Runner(
        agent=root_agent,
        app_name="test_agent",
        session_service=session_service,
    )

    user_message = Content(role="user", parts=[Part(text=prompt)])
    print(f"\nPrompt: {prompt}\n{'=' * 60}\n")

    async for event in runner.run_async(
        user_id="user", session_id="session-1", new_message=user_message
    ):
        if event.is_final_response() and event.content:
            for part in event.content.parts:
                if part.text:
                    print(part.text)


def main() -> None:
    parser = argparse.ArgumentParser(description="Test-Agent ADK runner")
    parser.add_argument(
        "--project",
        default="CRED",
        help="Jira project key to fetch stories from (default: CRED)",
    )
    parser.add_argument(
        "--status",
        default="Ready For Test",
        help='Jira story status filter (default: "Ready For Test")',
    )
    parser.add_argument(
        "--web",
        action="store_true",
        help="Launch the ADK web UI instead of running in CLI mode",
    )
    args = parser.parse_args()

    if args.web:
        import subprocess
        import sys
        subprocess.run([sys.executable, "-m", "adk", "web"], check=True)
        return

    prompt = build_prompt(args.project, args.status)
    asyncio.run(run_agent(prompt))


if __name__ == "__main__":
    main()
