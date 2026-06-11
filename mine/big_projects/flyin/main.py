import sys
from parser.parser import Parser
from parser.validator import Validator
from simulation.dijkstra import Algo
from simulation.graph_builder import GraphBuilder


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

    # Graph builder
    gbuild = GraphBuilder(zones, conns)
    graph = gbuild.build_graph()

    # Algo
    algo = Algo(zones, graph)
    res = algo.load(validator.start)
    dis = algo.distances

    print(graph)

except KeyboardInterrupt as e:
    print(e)
