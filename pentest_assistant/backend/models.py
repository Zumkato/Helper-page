"""Pydantic models for request/response bodies."""

from pydantic import BaseModel
from typing import Optional


class Target(BaseModel):
    host: str
    notes: Optional[str] = None


class Finding(BaseModel):
    title: str
    impact: Optional[str] = None
    remediation: Optional[str] = None
