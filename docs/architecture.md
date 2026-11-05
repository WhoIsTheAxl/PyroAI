# Architecture Notes

This document records the current architectural direction. It is a design guide, not a promise that every proposed feature is implemented.

## Environment

An environment is an interactive sandbox that contains or simulates a world. It owns its internal state and decides what information and capabilities are exposed to an agent.

An environment should be able to provide:
- Observations: the information visible to the agent.
- Tasks: objectives that can be assigned in that environment.
- Actions: operations an agent may perform.
- Feedback: results from actions and task progress.
- Episode / task completion signals.

The internal environment state does not have to be fully observable. An environment may expose only a partial observation.

## Task and action are distinct

A **task** describes the objective. An **action** is an operation the agent performs while pursuing that objective. A task may require a sequence of actions and may expose a set of actions that are valid in its current context.

For example, a Tic-Tac-Toe task could be "win the match"; an action could be "place a mark at row 1, column 2".

The environment remains responsible for validating and applying actions.

## Agent and algorithm

An **agent** interacts with an environment: it receives observations and selects actions.

An **algorithm** determines how the agent selects actions or improves its behavior. Algorithms should depend on stable PyroAI interfaces rather than a specific environment implementation.

Not every algorithm requires a neural network. Search, tabular learning, and optimization methods should not be forced to initialize a tensor backend.

## Training

The training subsystem should coordinate interaction, learning updates, evaluation, metrics, and checkpointing without owning environment-specific rules.

## Backends

Numerical and neural-network computation should be behind a backend boundary. PyTorch is not a required dependency. Lightweight backends and a CPU-friendly path are priorities; actual backend choices will be evaluated for platform support, installation size, and performance.

## Integrations

PyroAI should provide native environments while also allowing adapters for external environment APIs. Integrations should translate external observations, actions, and episode results into PyroAI's abstractions without requiring users to rewrite their environments.
