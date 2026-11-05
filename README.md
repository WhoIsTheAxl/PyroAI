# PyroAI

**PyroAI** is a fast, lightweight, and modular Python library for training specialized AI agents.

It is designed for **puzzle solving, games, simulations, and task-oriented intelligence**—not large language models or generative AI.

PyroAI aims to make it straightforward to create an environment, define what an agent can observe, give it a task, and train it to solve that task.

> **Project status:** Early development. The package structure and architecture are being established; public APIs and algorithms are not yet stable.

## Design goals

- **Lightweight:** Keep the core small and avoid unnecessary dependencies.
- **Accessible:** Make common training workflows approachable.
- **Extensible:** Support custom environments, tasks, actions, algorithms, and backends.
- **Portable:** Treat CPU-only systems and constrained devices, including Termux, as important targets.
- **Backend-flexible:** Use lightweight numerical / neural-network backends where needed; PyTorch is not a required dependency.
- **Algorithm-flexible:** Support approaches that do not require neural networks, as well as neural-network-based methods.

## Core concepts

- **Environment:** An interactive sandbox or world. It controls its internal state and exposes observations and available capabilities to an agent.
- **Observation:** The information an agent is allowed to perceive about an environment.
- **Task:** An objective the agent is asked to accomplish. A task can involve multiple actions.
- **Action:** An operation the agent performs within an environment.
- **Feedback:** The result of an action or progress toward a task, potentially including rewards.
- **Agent:** The decision-making system that observes an environment and chooses actions.
- **Algorithm:** The method used to make an agent learn, search, plan, or improve.
- **Trainer:** The component coordinating training and evaluation.

Tasks and actions are separate concepts: a task describes **what should be accomplished**, while actions describe **what the agent can do**.

## Intended applications

- Board games such as Tic-Tac-Toe
- Puzzle solving, including Rubik's Cubes
- Maze navigation and pathfinding
- Simulations and interactive tasks
- Optimization and decision-making problems

## Planned architecture

```text
src/pyroai/
├── core/          # Shared interfaces and fundamental types
├── environments/  # Native environments and external adapters
├── algorithms/    # Learning, search, and optimization methods
├── models/        # Agent model implementations
├── backends/      # Lightweight numerical / neural computation backends
├── training/      # Training, evaluation, and metrics
└── storage/       # Checkpoints and persistence
```

This layout is an initial scaffold and may evolve as the design is validated.

## Installation

PyroAI is not published on PyPI yet. For development, clone the repository and install it in editable mode:

```bash
git clone https://github.com/WhoIsTheAxl/PyroAI.git
cd PyroAI
python -m pip install -e .
```

The initial scaffold has no mandatory third-party runtime dependencies.

## Development

Run the test suite with:

```bash
python -m unittest discover -s tests
```

## License

PyroAI is licensed under the [Apache License 2.0](LICENSE).

Copyright © 2026 Axl. See [NOTICE](NOTICE) for project attribution.
