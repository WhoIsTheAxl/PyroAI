# PyroAI

**PyroAI** is a lightweight, modular Python library for building and training specialized agents for games, puzzles, simulations, and optimization tasks.

> **Status:** Early development. The core data contracts and a playable Tic-Tac-Toe environment are being implemented. Agent algorithms, trainers, and numerical backends are planned next.

## Principles

- Small standard-library-first core.
- CPU-first and portability-conscious, including constrained environments such as Termux.
- No mandatory PyTorch dependency.
- Tasks describe objectives; actions describe operations.
- Environments own their state and execute actions.
- Algorithms that do not need neural networks should not need a tensor backend.

## Core concepts

- **Environment:** Owns simulation state, manages task instances, validates and executes actions, and produces observations.
- **TaskDefinition:** Reusable description of an objective.
- **TaskInstance:** One attempt at a task, managed by an environment.
- **Action:** Immutable descriptor of an intended operation.
- **Observation:** Deeply read-only snapshot of agent-visible information.
- **Feedback:** Result of processing an action; reward is optional.
- **StepResult:** Feedback and the resulting observation in one response.
- **Experience:** Standardized record of one interaction transition.
- **Agent / Algorithm / Model / Backend:** Planned modular decision-making and computation layers.

## Install for development

```bash
git clone https://github.com/WhoIsTheAxl/PyroAI.git
cd PyroAI
python -m pip install -e .
```

PyroAI is not published on PyPI yet. The core has no mandatory third-party runtime dependencies.

## Run tests

```bash
python -m unittest discover -s tests -v
```

## Try the Tic-Tac-Toe environment

```python
from pyroai.core import Action, TaskDefinition
from pyroai.environments import TicTacToeEnvironment

env = TicTacToeEnvironment()
observation = env.reset(TaskDefinition(name="Play a match"))
result = env.execute(Action("place", {"row": 0, "column": 0}))
print(result.feedback.status, result.observation.data["board"])
```

## Project layout

```text
src/pyroai/
├── core/          # Shared immutable data types and task lifecycle
├── environments/  # Environment interface and native environments
├── algorithms/    # Learning, search, and optimization (planned)
├── models/        # Reusable models (planned)
├── backends/      # Optional compute backends (planned)
├── training/      # Training and evaluation (planned)
└── storage/       # Persistence and checkpoints (planned)
```

## License

Apache-2.0. Copyright 2026 Axl. See [LICENSE](LICENSE) and [NOTICE](NOTICE).