import json
import requests
from google.adk.tools import FunctionTool


def send_api_request(
    method: str,
    url: str,
    headers: dict = None,
    body: dict = None,
    expected_status: int = 200,
) -> dict:
    """Send an HTTP request and return the response details.

    Args:
        method: HTTP method (GET, POST, PUT, DELETE, PATCH).
        url: Full URL to send the request to.
        headers: Optional request headers as a dict.
        body: Optional request body as a dict (sent as JSON).
        expected_status: Expected HTTP status code for pass/fail determination.

    Returns:
        A dict with keys: status_code, response_body, headers, passed, error.
    """
    try:
        response = requests.request(
            method=method.upper(),
            url=url,
            headers=headers or {},
            json=body,
            timeout=30,
        )
        return {
            "status_code": response.status_code,
            "response_body": response.text,
            "headers": dict(response.headers),
            "passed": response.status_code == expected_status,
            "error": None,
        }
    except requests.exceptions.RequestException as e:
        return {
            "status_code": None,
            "response_body": None,
            "headers": {},
            "passed": False,
            "error": str(e),
        }


def assert_json_field(response_body: str, field_path: str, expected_value: str) -> dict:
    """Assert that a JSON field in a response body matches an expected value.

    Args:
        response_body: Raw JSON string of the response body.
        field_path: Dot-separated path to the field (e.g. "data.id").
        expected_value: Expected string value of the field.

    Returns:
        A dict with keys: passed, actual_value, error.
    """
    try:
        data = json.loads(response_body)
        keys = field_path.split(".")
        value = data
        for key in keys:
            value = value[key]
        actual = str(value)
        return {"passed": actual == expected_value, "actual_value": actual, "error": None}
    except (json.JSONDecodeError, KeyError, TypeError) as e:
        return {"passed": False, "actual_value": None, "error": str(e)}


api_tool_set = [
    FunctionTool(send_api_request),
    FunctionTool(assert_json_field),
]
