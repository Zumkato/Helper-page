"""Utilities to summarize raw notes or tool output."""

from . import llm


def to_report(text: str) -> str:
    """Return report-ready text for the provided raw input."""
    return llm.summarize_text(text)
