# Repository Guidelines

## Project Structure & Module Organization

This repository contains automation for discovering, downloading, and converting Bundesrechnungshof reports to Markdown. Source code lives in `src/brh_reports/`, with the CLI entry point in `cli.py` and pipeline orchestration in `pipeline.py`. Tests are in `tests/` and mirror the package behavior by area, for example `test_cli.py`, `test_crawler.py`, and `test_repository.py`.

Generated content is stored under `reports/markdown/<year>/` and `reports/metadata/`. Runtime state is tracked in `state/processed_reports.json`; keep this file consistent with report outputs. Temporary download data belongs outside version control or under ignored paths such as `data/tmp/`.

## Build, Test, and Development Commands

Set up a local editable environment:

```powershell
python -m pip install -e .[dev]
```

Run the test suite:

```powershell
python -m pytest
```

Run linting:

```powershell
python -m ruff check .
```

Run the report automation:

```powershell
python -m brh_reports run
python -m brh_reports discover
python -m brh_reports download
```

The installed console script `brh-reports` exposes the same commands.

## Coding Style & Naming Conventions

Use Python 3.14 syntax. Follow Ruff defaults in `pyproject.toml`, including a 100-character line length. Use 4-space indentation, `snake_case` for functions and variables, `PascalCase` for classes and dataclasses, and explicit type hints for public helpers. Keep filesystem paths as `pathlib.Path` objects rather than raw strings when adding repository logic.

## Testing Guidelines

Tests use `pytest`; place new tests in `tests/` with filenames matching `test_*.py`. Prefer small, deterministic tests using `tmp_path` for filesystem behavior. Avoid live network access in unit tests; mock crawler, downloader, or converter boundaries when testing orchestration. Run `python -m pytest` before submitting changes, and add regression tests for changes to report identity, manifest handling, parsing, or CLI behavior.

## Commit & Pull Request Guidelines

Existing history uses short, descriptive subjects such as `reports` and `2025 reports`. Keep commits focused and concise; for automated report syncs, the workflow pattern is `YYYY-MM-DD sync Bundesrechnungshof reports`.

Pull requests should describe the behavior changed, list validation commands run, and call out any generated changes under `reports/` or `state/`. Link related issues when applicable. Include screenshots only for documentation or rendered-output changes where visual review adds value.

## Security & Configuration Tips

Do not commit virtual environments, caches, temporary PDFs, or local browser artifacts. The sync workflow sets `PLAYWRIGHT_BROWSERS_PATH=0`; keep browser dependencies reproducible when changing crawler behavior. Be conservative with request timing and user-agent changes in `config.py`.
