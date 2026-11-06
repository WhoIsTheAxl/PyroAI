"""Base contract for interactive PyroAI environments."""
from abc import ABC, abstractmethod
from pyroai.core import Action, Observation, StepResult, TaskDefinition, TaskInstance

class Environment(ABC):
    """Owns simulation state, active tasks, action execution, and observations."""
    def __init__(self):
        self._task: TaskInstance | None = None

    @property
    def task(self):
        """Current task instance, if one has been created."""
        return self._task

    def create_task(self, definition: TaskDefinition) -> TaskInstance:
        """Create and activate a task instance for this environment."""
        if not isinstance(definition, TaskDefinition): raise TypeError("definition must be TaskDefinition")
        if self._task is not None and self._task.status.value in ("pending", "active"): raise RuntimeError("environment already has an unfinished task")
        self._task = TaskInstance(definition)
        self._task.start()
        return self._task

    @abstractmethod
    def reset(self, task: TaskDefinition | None = None) -> Observation:
        """Reset the environment and return the initial observation."""
        raise NotImplementedError

    @abstractmethod
    def observe(self, agent=None) -> Observation:
        """Return an agent-visible snapshot; agent may customize visibility."""
        raise NotImplementedError

    @abstractmethod
    def execute(self, action: Action, agent=None) -> StepResult:
        """Validate and execute an action, returning feedback and observation."""
        raise NotImplementedError

    def close(self) -> None:
        """Release resources. Native in-memory environments need no action."""
        return None