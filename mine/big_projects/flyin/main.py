import sys
from parser.parser import Parser
from parser.validator import Validator
from simulation.path_finder import PathFinder


try:
    # Parser
    file_path = sys.argv[1]
    parser = Parser(file_path)
    parser.load()

    # Validator
    validator = Validator(
        parser.zones,
        parser.connections
    )

    # kind, name, x, y, meta_data
    zones = validator.zones_obj()
    conns = validator.connection_obj()

    # Paths finder
    paths = PathFinder(zones, conns, validator.start, validator.end)
    paths.load()
    res = paths.get_multiple_paths()
    for r in res:
        print(r)

except KeyboardInterrupt as e:
    print(e)
