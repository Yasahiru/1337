import sys
import site
import os


def main() -> None:
    try:
        if sys.prefix == sys.base_prefix:
            print("MATRIX STATUS: You're still plugged in\n")
            print(f"Current Python: {sys.executable}")
            print("Virtual Environment: None detected\n")
            print("WARNING: You're in the global environment!")
            print("The machines can see everything you install.\n")
            print("To enter the construct, run:")
            print("python -m venv matrix_env")
            print("source matrix_env/bin/activate # On Unix")
            print(r"matrix_env\Scripts\activate # On Windows")
            print()
            print("Then run this program again.")
        else:
            print()
            print("MATRIX STATUS: Welcome to the construct")
            print()
            print(f"Current Python: {sys.executable}")
            print(f"Virtual Environment: {os.path.basename(sys.prefix)}")
            print(f"Environment Path: {sys.prefix}")
            print()
            print("SUCCESS: You're in an isolated environment!")
            print("Safe to install packages without affecting")
            print("the global system.")
            print()
            print(f"Package installation path: {site.getsitepackages()[0]}")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
