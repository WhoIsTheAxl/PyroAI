"""Structured action outcomes."""
from dataclasses import dataclass, field
from enum import Enum
from numbers import Real
from typing import Any, Mapping
from ._immutability import freeze_mapping

class FeedbackStatus(str, Enum):
    SUCCESS = "success"
    REJECTED = "rejected"
    ERROR = "error"

@dataclass(frozen=True, slots=True)
class Feedback:
    """Outcome of processing an action. Reward is optional."""
    accepted: bool
    status: FeedbackStatus
    data: Mapping[str, Any] = field(default_factory=dict)
    reason: str | None = None
    reward: float | None = None

    def __post_init__(self):
        if not isinstance(self.accepted, bool): raise TypeError("accepted must be bool")
        if not isinstance(self.status, FeedbackStatus): raise TypeError("status must be FeedbackStatus")
        if self.accepted != (self.status is FeedbackStatus.SUCCESS): raise ValueError("accepted must be true exactly for SUCCESS")
        if self.reason is not None and not isinstance(self.reason, str): raise TypeError("reason must be str or None")
        if self.reward is not None:
            if isinstance(self.reward, bool) or not isinstance(self.reward, Real): raise TypeError("reward must be a real number or None")
            object.__setattr__(self, "reward", float(self.reward))
        object.__setattr__(self, "data", freeze_mapping(self.data, "data"))