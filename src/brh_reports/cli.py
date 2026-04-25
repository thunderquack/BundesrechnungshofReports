from __future__ import annotations

import argparse

from brh_reports.pipeline import discover_pipeline, download_pipeline, run_pipeline


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="brh-reports",
        description="Bundesrechnungshof report downloader and converter.",
    )
    parser.add_argument(
        "command",
        choices=["run", "discover", "download"],
        nargs="?",
        default="run",
        help="Pipeline command to execute.",
    )
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    if args.command == "run":
        return run_pipeline()
    if args.command == "discover":
        discover_pipeline()
        return 0
    if args.command == "download":
        return download_pipeline()

    parser.error(f"Unsupported command: {args.command}")
    return 2
