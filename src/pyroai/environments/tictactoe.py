"""A small native Tic-Tac-Toe environment for smoke tests and examples."""
from pyroai.core import (
    Action, Feedback, FeedbackStatus, Observation, StepResult,
    TaskDefinition, TaskOutcome, TaskStatus,
)
from .base import Environment

class TicTacToeEnvironment(Environment):
    """Two-player, 3x3 Tic-Tac-Toe with X moving first."""
    def __init__(self):
        super().__init__()
        self._board = None
        self._current_player = None

    def reset(self, task: TaskDefinition | None = None) -> Observation:
        """Start a fresh match, cancelling any unfinished previous task."""
        if self.task is not None and self.task.status in (TaskStatus.PENDING, TaskStatus.ACTIVE):
            self.task.cancel()
        if task is None: task = TaskDefinition(name="Play Tic-Tac-Toe", goal="Complete the match")
        self.create_task(task)
        self._board = [[None for _ in range(3)] for _ in range(3)]
        self._current_player = "X"
        return self.observe()

    def observe(self, agent=None) -> Observation:
        """Return a detached, read-only board snapshot."""
        if self._board is None: raise RuntimeError("call reset() before observe()")
        return Observation({
            "board": self._board,
            "current_player": self._current_player,
            "winner": self._winner(),
            "is_draw": self._is_draw(),
        })

    def execute(self, action: Action, agent=None) -> StepResult:
        """Apply a place action or return a rejected result without mutation."""
        if self._board is None or self.task is None: raise RuntimeError("call reset() before execute()")
        if self.task.status is not TaskStatus.ACTIVE: raise RuntimeError("task is not active")
        if not isinstance(action, Action): raise TypeError("action must be an Action")
        if action.type != "place": return self._reject("unsupported action type")
        row, column = action.parameters.get("row"), action.parameters.get("column")
        if isinstance(row, bool) or not isinstance(row, int) or isinstance(column, bool) or not isinstance(column, int): return self._reject("row and column must be integers")
        if not (0 <= row < 3 and 0 <= column < 3): return self._reject("coordinates are outside the board")
        if self._board[row][column] is not None: return self._reject("cell is occupied")
        self._board[row][column] = self._current_player
        winner = self._winner()
        if winner is not None:
            self.task.complete(TaskOutcome.SUCCESS)
            feedback = Feedback(True, FeedbackStatus.SUCCESS, data={"placed": self._current_player, "winner": winner}, reward=1.0)
        elif self._is_draw():
            self.task.complete(TaskOutcome.NEUTRAL)
            feedback = Feedback(True, FeedbackStatus.SUCCESS, data={"placed": self._current_player, "draw": True}, reward=0.0)
        else:
            feedback = Feedback(True, FeedbackStatus.SUCCESS, data={"placed": self._current_player})
            self._current_player = "O" if self._current_player == "X" else "X"
        return self._result(feedback)

    def _reject(self, reason):
        return self._result(Feedback(False, FeedbackStatus.REJECTED, reason=reason))

    def _result(self, feedback):
        return StepResult(feedback, self.observe(), self.task.status, self.task.outcome)

    def _winner(self):
        lines = list(self._board)
        lines += [[self._board[r][c] for r in range(3)] for c in range(3)]
        lines += [[self._board[i][i] for i in range(3)], [self._board[i][2-i] for i in range(3)]]
        for line in lines:
            if line[0] is not None and line.count(line[0]) == 3: return line[0]
        return None

    def _is_draw(self):
        return self._winner() is None and all(cell is not None for row in self._board for cell in row)