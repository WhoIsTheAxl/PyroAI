# Architecture

This document describes the current API direction. Implemented components are usable; planned components are explicitly marked.

## Environment and tasks

An Environment owns internal state and manages TaskInstances. A TaskDefinition is a reusable objective specification; each TaskInstance represents one attempt. The definition describes the goal, while the environment evaluates it against its own state.

## Actions

Action is an immutable data descriptor, not executable behavior. It performs structural validation. The environment performs contextual validation and execution.

## Observations

Observation is a read-only snapshot of information exposed to an agent, not a reference to internal environment state. Nested mappings and sequences are frozen. `mutable_copy()` returns detached data for preprocessing.

## Feedback and StepResult

Feedback reports whether an action was accepted and its outcome. `SUCCESS`, `REJECTED`, and `ERROR` are distinct. Reward is optional. StepResult bundles Feedback with the post-step Observation and task lifecycle information.

## Experience

Experience stores the previous observation, action, feedback, next observation, and task state. Algorithms may use this common record or derive algorithm-specific representations.

## Agent, Algorithm, Model, Backend (planned)

Agents may implement custom decision logic or delegate to an optional Algorithm. Models are independent components whose lifecycle may be managed by an Agent or Algorithm. Backends provide optional numerical computation. Search and tabular algorithms must not be forced to use neural-network backends.

## Training and integrations (planned)

Training coordinates interaction, updates, evaluation, metrics, and checkpoints. Adapters translate external environment APIs into PyroAI's contracts.