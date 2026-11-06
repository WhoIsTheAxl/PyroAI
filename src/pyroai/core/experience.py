"""Standardized record of an agent-environment transition."""
from dataclasses import dataclass, field
from typing import Any, Mapping
from ._immutability import freeze_mapping
from .action import Action
from .feedback import Feedback
from .observation import Observation
from .task import TaskOutcome, TaskStatus

@dataclass(frozen=True, slots=True)
class Experience:
    """One transition, extensible through metadata or algorithm adapters."""
    observation: Observation
    action: Action
    feedback: Feedback
    next_observation: Observation
    task_status: TaskStatus
    task_outcome: TaskOutcome | None = None
    metadata: Mapping[str, Any] = field(default_factory=dict)

    def __post_init__(self):
        if not isinstance(self.observation, Observation): raise TypeError("observation must be Observation")
        if not isinstance(self.action, Action): raise TypeError("action must be Action")
        if not isinstance(self.feedback, Feedback): raise TypeError("feedback must be Feedback")
        if not isinstance(self.next_observation, Observation): raise TypeError("next_observation must be Observation")
        if not isinstance(self.task_status, TaskStatus): raise TypeError("task_status must be TaskStatus")
        if self.task_status is TaskStatus.COMPLETED and not isinstance(self.task_outcome, TaskOutcome): raise ValueError("completed task requires an outcome")
        if self.task_status is not TaskStatus.COMPLETED and self.task_outcome is not None: raise ValueError("only completed tasks have an outcome")
        object.__setattr__(self, "metadata", freeze_mapping(self.metadata, "metadata"))