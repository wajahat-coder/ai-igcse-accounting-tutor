# Copilot / AI Agent Instructions — ai-igcse-accounting-tutor

Purpose
- Short, actionable guidance for autonomous coding agents working in this repository.

Repo state
- At time of generation there are no application source files discovered in the workspace root. Agents should run the discovery steps below before making changes.

Discovery steps (first actions for any session)
- List top-level files and folders: `ls -la` or inspect the workspace tree.
- Look for these files (in order): `README.md`, `package.json`, `pyproject.toml`, `requirements.txt`, `setup.py`, `Pipfile`, `src/`, `app/`, `services/`, `Dockerfile`, `.github/workflows/`.
- If a manifest is present (`package.json`, `pyproject.toml`, `requirements.txt`) report detected language/runtime and any test/build scripts.

How to understand architecture (when code exists)
- Identify entrypoints: look for `src/main`, `app.py`, `index.js`, or `server.ts`.
- Grouping convention: expect logical folders like `src/`, `services/`, `client/`, `server/`. Treat each as a component boundary.
- Data flow: follow models/schemas and API route handlers to map request → service → persistence layers.

Developer workflows (what agents should run and report)
- If `package.json` exists: read `scripts` and run `npm test` only after user approval.
- If Python manifests exist: prefer `python -m pytest` if `pytest` is listed; otherwise run `python -m unittest discover` only with approval.
- If CI workflows exist in `.github/workflows/`, summarize key build/test steps before altering config.

Project-specific conventions
- If tests exist, run only targeted tests related to changed files. Do not run the entire test suite without permission.
- Keep changes minimal and focused. Open a PR-style patch with a single logical change per file.

Integration points & external dependencies
- Search for `.env`, `.env.example`, `secrets` or `config` folders. Never attempt to access real secrets — ask the user to provide redacted values or run tasks locally.
- If Dockerfile or deployment manifests exist, summarize intended runtime image and exposed ports before modifying.

Editing rules for AI agents
- Do not commit or push without an explicit instruction. Prepare patches via `apply_patch` and present them for review.
- When adding new dependencies, include an update to the manifest file and a short rationale in the change description.

What to include in PR/patch descriptions
- Purpose of the change (1 line). Files changed (bullet list). How to verify (commands or test names). Any migration or env changes.

If you encounter an empty repository
- Summarize what files are missing and propose a minimal scaffold (e.g., `README.md`, basic `src/` layout, `requirements.txt` or `package.json`). Ask the user whether to scaffold.

Where to update this guidance
- Edit this file at [.github/copilot-instructions.md](.github/copilot-instructions.md) with new, discovered, project-specific rules.

If anything here is unclear or you want more project-specific examples, ask the user to point to key files to inspect and I will update this file accordingly.
