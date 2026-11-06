"""Reusable task definitions and environment-managed task instances."""
from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Mapping
from uuid import uuid4
from ._immutability import freeze_mapping

class TaskStatus(str, Enum):
    PENDING = "pending"
    ACTIVE = "active"
    COMPLETED = "completed"
    CANCELLED = "cancelled"

class TaskOutcome(str, Enum):
    SUCCESS = "success"
    FAILURE = "failure"
    NEUTRAL = "neutral"

@dataclass(frozen=True, slots=True)
class TaskDefinition:
    """Reusable objective specification, independent of environment logic."""
    name: str
    description: str = ""
    goal: str | None = None
    metadata: Mapping[str, Any] = field(default_factory=dict)

    def __post_init__(self):
        if not isinstance(self.name, str) or not self.name.strip(): raise ValueError("task name must be a non-empty string")
        if not isinstance(self.description, str): raise TypeError("description must be a string")
        if self.goal is not None and not isinstance(self.goal, str): raise TypeError("goal must be str or None")
        object.__setattr__(self, "metadata", freeze_mapping(self.metadata, "metadata"))

@dataclass(slots=True)
class TaskInstance:
    """One attempt to complete a task definition."""
    definition: TaskDefinition
    id: str = field(default_factory=lambda: uuid4().hex)
    status: TaskStatus = TaskStatus.PENDING
    outcome: TaskOutcome | None = None

    def __post_init__(self):
        if not isinstance(self.definition, TaskDefinition): raise TypeError("definition must be TaskDefinition")
        if not isinstance(self.id, str) or not self.id: raise ValueError("id must be a non-empty string")
        if self.status is not TaskStatus.PENDING or self.outcome is not None: raise ValueError("new instances must be pending")

    def start(self):
        if self.status is not TaskStatus.PENDING: raise RuntimeError("only pending tasks can start")
        self.status = TaskStatus.ACTIVE

    def complete(self, outcome):
        if self.status is not TaskStatus.ACTIVE: raise RuntimeError("only active tasks can complete")
        if not isinstance(outcome, TaskOutcome): raise TypeError("outcome must be TaskOutcome")
        self.status, self.outcome = TaskStatus.COMPLETED, outcome

    def cancel(self):
        if self.status not in (TaskStatus.PENDING, TaskStatus.ACTIVE): raise RuntimeError("only pending or active tasks can be cancelled")
        self.status = TaskStatus.CANCELLED