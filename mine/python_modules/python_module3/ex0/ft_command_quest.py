import sys


def main() -> None:
    print("=== Command Quest ===")
    if (len(sys.argv) <= 1):
        print("No arguments provided!")
        print(f"Program name: {sys.argv[0]}")
    else:
        count: int = 1
        print(f"Program name: {sys.argv[0]}")
        print(f"Arguments recived: {len(sys.argv) - 1}")
        for av in sys.argv:
            if (av != sys.argv[0]):
                print(f"Argument {count}: {av}")
                count += 1
    print(f"Total arguments: {len(sys.argv)}")


if __name__ == "__main__":
    main()
