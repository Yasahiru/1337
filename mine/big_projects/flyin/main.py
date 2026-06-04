import argparse
from pathlib import Path

from simulation import run_simulation


def build_parser() -> argparse.ArgumentParser:
    desc = "Load a map file, run the drone simulator, and print "
    desc += "turn-by-turn moves."

    parser = argparse.ArgumentParser(
        description=desc
    )
    parser.add_argument("file_path", help="Path to the input map file")
    return parser


def main() -> None:
    args = build_parser().parse_args()
    file_path = Path(args.file_path)

    if not file_path.exists():
        raise FileNotFoundError(f"Input file does not exist: {file_path}")

    result_lines, total_turns = run_simulation(str(file_path))

    for line in result_lines:
        print(line)

    print(f"Total turns: {total_turns}")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
