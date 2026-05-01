from typing import Final
import sys


dependencies: dict[str, str] = {
        "pandas": "Data manipulation ready",
        "numpy": "Numerical computation ready",
        "matplotlib": "Visualization ready",
        "requests": "Network access ready"
    }

missing: list[str] = []


def dependencie_check() -> None:
    print("Checking dependencies:")
    try:
        import importlib.metadata
        import importlib.util
    except Exception as e:
        print(e)

    for pkg, status in dependencies.items():
        spec = importlib.util.find_spec(pkg)
        if spec is not None:
            try:
                version = importlib.metadata.version(pkg)
                print(f"[OK] {pkg} ({version} - {status})")
            except importlib.metadata.PackageNotFoundError:
                print(f"[ERROR] {pkg} found but version inaccessible.")
                missing.append(pkg)
        else:
            print()
            print("CRITICAL FAILURE: Missing dependencies: ")
            miss = []
            for pkg in dependencies:
                if not importlib.util.find_spec(pkg):
                    miss.append(pkg)
            print(f"    {', '.join(miss)}")
            print()
            print("To enter the construct with all programs, run:")
            print("For pip users:    pip install -r requirements.txt")
            print("For Poetry users: poetry install")
            print()
            sys.exit(1)


DATA_POINTS: Final[int] = 1000


def fetch_matrix_data() -> None:
    """
    Analyzes the distribution of Matrix signals using a Histogram.
    """
    try:
        import pandas as pd  # type: ignore
        import numpy as np  # type: ignore
        import matplotlib.pyplot as plt  # type: ignore
    except Exception as e:
        print(e)
    try:
        print(
            "Analyzing Matrix data... Processing "
            f"{DATA_POINTS} data points..."
        )
        raw_signals: np.ndarray = np.random.normal(
            loc=0, scale=1, size=DATA_POINTS
        )
        df: pd.DataFrame = pd.DataFrame(raw_signals, columns=['Frequency'])

        print("Generating visualization...")
        plt.figure(figsize=(10, 6))
        plt.hist(
            df['Frequency'],
            bins=50,
            color='purple',
            edgecolor='black',
            alpha=0.7
        )

        plt.title("Matrix Signal Frequency Distribution")
        plt.xlabel("Signal Intensity")
        plt.ylabel("Occurrences")
        plt.grid(axis='y', alpha=0.3)
        plt.savefig("matrix_analysis.png")
        print("Analysis complete! Results saved to: matrix_analysis.png")

    except Exception as e:
        print(f"CRITICAL ERROR: Data stream corrupted: {e}")


def main() -> None:
    print()
    print("LOADING STATUS: Loading programs...")
    dependencie_check()
    fetch_matrix_data()
    print("Analysis complete!")
    print("Results saved to: matrix_analysis.png")
    print()


if __name__ == "__main__":
    main()
