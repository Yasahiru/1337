import argparse
from pathlib import Path
from simulation.simulation import run_simulation

try:
    parser = argparse.ArgumentParser()
    parser.add_argument("file_path")
    file_path = Path(parser.parse_args().file_path)

    if not file_path.exists():
        raise FileNotFoundError(file_path)

    lines, turns = run_simulation(str(file_path))

    print("\n".join(lines))
    print("Total turns:", turns)

except Exception as e:
    print(e)
