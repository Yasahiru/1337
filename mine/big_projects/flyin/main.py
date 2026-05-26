import argparse
from pathlib import Path

from parser.parser import Parser
from parser.validator import Validator


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Load a map file, parse it, and print the parsed zones."
    )
    parser.add_argument("file_path", help="Path to the input map file")
    return parser


def main() -> None:
    args = build_parser().parse_args()
    file_path = Path(args.file_path)

    if not file_path.exists():
        raise FileNotFoundError(f"Input file does not exist: {file_path}")

    p = Parser(str(file_path))
    p.load()

    v = Validator(p.zones, p.connections)

    for z in v.zones_obj():
        print(z)


if __name__ == "__main__":
    main()
