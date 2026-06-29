# Bundesrechnungshof Reports

Automation for discovering, downloading, and converting Bundesrechnungshof PDF reports to Markdown.

## Requirements

- Python 3.14
- Playwright browser dependencies

## Setup

```powershell
py -3.14 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -e .[dev]
python -m playwright install
```

## Run

```powershell
python -m brh_reports run
```

This runs the full pipeline:

- discover report candidates;
- compare them with `state/processed_reports.json`;
- download new PDFs to a temporary system directory;
- convert new reports to Markdown;
- save Markdown under `reports/markdown/`;
- update `state/processed_reports.json`.

## Other Commands

```powershell
python -m brh_reports discover
python -m brh_reports download
```

## Output

- Markdown reports: `reports/markdown/`
- Processed state: `state/processed_reports.json`

## Notes

- GitHub Actions is currently frozen, so the pipeline is expected to run locally.
- Temporary PDFs are not stored in the repository.
