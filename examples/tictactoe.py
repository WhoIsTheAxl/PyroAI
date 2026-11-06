"""Play a short deterministic Tic-Tac-Toe match against the environment."""
from pyroai.core import Action
from pyroai.environments import TicTacToeEnvironment

env = TicTacToeEnvironment()
observation = env.reset()
for row, column in [(0, 0), (1, 0), (0, 1), (1, 1), (0, 2)]:
    result = env.execute(Action("place", {"row": row, "column": column}))
    observation = result.observation
    print(result.feedback.status.value, observation.data["board"])
    if result.task_status.value == 'completed':
        print('Outcome:', result.task_outcome.value)
        break