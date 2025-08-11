import asyncio
import pytest

from pentest_assistant.services import executor, llm


def test_executor_allowlist():
    """Allowed commands return mocked output and others raise."""
    result = asyncio.run(executor.run("nmap"))
    assert "nmap" in result
    with pytest.raises(ValueError):
        asyncio.run(executor.run("ls"))


def test_llm_echo():
    provider = llm.EchoLLM()
    prompt = "test prompt"
    resp = asyncio.run(provider.generate(prompt))
    assert prompt in resp
