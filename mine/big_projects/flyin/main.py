from parser.parser import Parser
from parser.validator import Validator
import sys


def main() -> None:
    file_path = sys.argv[1]
    p = Parser(file_path)
    p.load()

    v = Validator(p.zones, p.connections)

    for z in v.zones_obj():
        print(z)


if __name__ == "__main__":
    main()
