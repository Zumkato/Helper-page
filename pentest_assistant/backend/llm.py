"""Thin wrapper around LLM calls.

If the OpenAI SDK is not installed or no API key is present, the functions
fall back to simple placeholder responses so that the rest of the
application remains functional.
"""

import os

try:
    from openai import OpenAI
except Exception:  # pragma: no cover - we expect ImportError when deps missing
    OpenAI = None

_client = None
if OpenAI and os.getenv("OPENAI_API_KEY"):
    _client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])


def _fallback(message: str) -> str:
    """Return a basic fallback message when no LLM is configured."""
    return f"[LLM unavailable] {message}"


def suggest_attack_steps(context: dict) -> str:
    """Suggest next attack steps for the given context."""
    prompt = (
        "Given this foothold:\n"
        f"{context}\n"
        "Suggest next attack steps and relevant CVEs or tools."
    )
    if _client:
        resp = _client.responses.create(model="gpt-4o-mini", input=prompt)
        return resp.output[0].content[0].text
    return _fallback("No suggestions available.")


def generate_report(findings) -> str:
    prompt = f"Build an executive summary and remediation plan:\n{findings}"
    if _client:
        resp = _client.responses.create(model="gpt-4o-mini", input=prompt)
        return resp.output[0].content[0].text
    return _fallback("No report generated.")


def summarize_text(text: str) -> str:
    prompt = f"Summarize the following information:\n{text}"
    if _client:
        resp = _client.responses.create(model="gpt-4o-mini", input=prompt)
        return resp.output[0].content[0].text
    return _fallback("No summary available.")
