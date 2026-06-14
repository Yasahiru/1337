import sys
from parser.parser import Parser
from parser.validator import Validator
from simulation.path_finder import PathFinder
from simulation.simulator import Simulator


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
    mult_paths = paths.get_multiple_paths()

    # for k, v in paths.graph.items():
    #     print(k, v, sep=": ")
    print(mult_paths)

    sim = Simulator(
        nb_drones=parser.nb_drones,
        start=validator.start,
        paths=mult_paths,
        zones=zones,
        conns=conns,
        graph=paths.graph
    )
    sim.create_drones()

except KeyboardInterrupt as e:
    print(e)
