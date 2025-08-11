"""Very small in-memory storage layer used for demos and tests."""

from typing import List, Dict

_targets: List[Dict] = []
_findings: List[Dict] = []


def save_target(target: Dict) -> None:
    _targets.append(target)


def fetch_targets() -> List[Dict]:
    return list(_targets)


def save_finding(finding: Dict) -> None:
    _findings.append(finding)


def fetch_findings() -> List[Dict]:
    return list(_findings)
