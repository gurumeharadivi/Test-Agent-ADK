"""Shared Gemini model configuration used by all agents in the pipeline.

To switch models, change the model name here — no other files need updating.
Requires GOOGLE_API_KEY in .env for Google AI Studio backend.
"""

from google.adk.models.google_llm import Gemini
from google.genai.types import HttpRetryOptions

_retry_config = HttpRetryOptions(
    attempts=5,
    initial_delay=2.0,
    max_delay=60.0,
)

llm_model = Gemini(
    model="gemini-2.5-flash",
    retry_options=_retry_config,
)
