from brh_reports.cli import build_parser


def test_default_command_is_run() -> None:
    parser = build_parser()
    args = parser.parse_args([])
    assert args.command == "run"
