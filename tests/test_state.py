import asyncio
from pathlib import Path
import pytest

from pentest_assistant.db import DB_FILE, init_db
from pentest_assistant.state.project_state import ProjectState


def test_project_state_crud():
    if DB_FILE.exists():
        DB_FILE.unlink()
    init_db()
    state = ProjectState()
    proj = asyncio.run(state.create_project("Test Project", "desc"))
    assert proj["name"] == "Test Project"

    asyncio.run(state.load_project(proj["id"]))
    assert state.current_project["id"] == proj["id"]

    asyncio.run(state.handle_add_note({"content": "<b>bold</b>"}))
    assert state.notes and state.notes[-1]["content"] == "bold"
    # Ensure malicious HTML is stripped
    asyncio.run(state.handle_add_note({"content": "<script>alert('x')</script>note"}))
    assert "<" not in state.notes[-1]["content"]

    asyncio.run(state.handle_run_command({"command": "nmap"}))
    assert state.runs and state.runs[-1]["command"] == "nmap"

    resp = asyncio.run(state.suggest_chain_steps("test"))
    assert "test" in resp

    # Reload project and confirm notes remain sanitized
    asyncio.run(state.load_project(proj["id"]))
    assert all("<" not in n["content"] for n in state.notes)

    # Export report and verify output contains notes and chain steps
    state.add_chain_step("Initial reconnaissance")
    paths = asyncio.run(state.export_report())
    md_path = paths["markdown_path"]
    assert Path(md_path).exists()
    text = Path(md_path).read_text()
    assert "Initial reconnaissance" in text
    assert "bold" in text

