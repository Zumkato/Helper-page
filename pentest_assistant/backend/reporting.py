"""Tools for assembling findings into a Markdown report."""

from typing import List, Dict
import markdown2


def findings_to_markdown(findings: List[Dict]) -> str:
    """Convert findings into a very small Markdown document."""
    lines = ["# Findings", ""]
    for item in findings:
        lines.append(f"- {item.get('title', 'Untitled')} : {item.get('impact', '')}")
    return "\n".join(lines)


def markdown_to_html(markdown_text: str) -> str:
    return markdown2.markdown(markdown_text)
