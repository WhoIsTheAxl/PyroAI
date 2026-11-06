"""Combined result of one environment interaction."""
from dataclasses import dataclass
from .feedback import Feedback
from .observation import Observation
from .task import TaskOutcome, TaskStatus

@dataclass(frozen=True, slots=True)
class StepResult:
    """Feedback plus the resulting observation and task state."""
    feedback: Feedback
    observation: Observation
    task_status: TaskStatus
    task_outcome: TaskOutcome | None = None

    def __post_init__(self):
        if not isinstance(self.feedback, Feedback): raise TypeError("feedback must be Feedback")
        if not isinstance(self.observation, Observation): raise TypeError("observation must be Observation")
        if not isinstance(self.task_status, TaskStatus): raise TypeError("task_status must be TaskStatus")
        if self.task_status is TaskStatus.COMPLETED and not isinstance(self.task_outcome, TaskOutcome): raise ValueError("completed task requires an outcome")
        if self.task_status is not TaskStatus.COMPLETED and self.task_outcome is not None: raise ValueError("only completed tasks have an outcome")