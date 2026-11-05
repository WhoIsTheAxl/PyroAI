# Contributing to PyroAI

Thanks for your interest in PyroAI!

The project is in early development, so its APIs and architecture may change.

## Before contributing

1. Read the project overview in [README.md](README.md).
2. Review the current design notes in [docs/architecture.md](docs/architecture.md).
3. Open an issue or discussion before making large architectural changes.

## Development setup

```bash
git clone https://github.com/WhoIsTheAxl/PyroAI.git
cd PyroAI
python -m pip install -e .
python -m unittest discover -s tests
```

## Contribution guidelines

- Keep the core lightweight and avoid unnecessary mandatory dependencies.
- Preserve portability, including compatibility with constrained CPU-only environments.
- Keep environment-specific behavior out of generic algorithms.
- Keep tasks (objectives) distinct from actions (operations).
- Add or update tests when changing behavior.
- Document public APIs and note breaking changes.

By submitting a contribution, you agree that it is provided under the project's Apache-2.0 license, unless a separate written agreement says otherwise.
