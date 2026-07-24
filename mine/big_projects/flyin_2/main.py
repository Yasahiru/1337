import sys
from parser import Parser
from validator import Validator
from path_finder import PathFinder
from simulator import Simulator
from visualizer import Visualizer


class Main:

    def run(self) -> None:
        # Parser
        file_path = sys.argv[1]
        parser = Parser(file_path)
        parser.load()

        # Validator
        _zones = parser.zones
        _conns = parser.connections
        validator = Validator(_zones, _conns)

        # kind, name, x, y, meta_data
        zones = validator.zones_obj()
        conns = validator.connection_obj()

        # Paths finder
        if validator.start is None or validator.end is None:
            raise ValueError("Missing start or end zone definition")

        paths = PathFinder(zones, conns, validator.start, validator.end)
        paths.load()

        mult_paths = paths.get_multiple_paths()

        sim = Simulator(
            nb_drones=parser.nb_drones,
            start=validator.start,
            end=validator.end,
            paths=mult_paths,
            zones=zones,
            conns=conns,
            graph=paths.graph
        )
        sim.create_drones()
        sim.assign_drones_to_paths()

        sim.run()
        sim.get_output()

        v = Visualizer(
            sim.zones,
            sim.conns,
            sim.frames
        )
        v.run()


if __name__ == "__main__":
    try:
        main = Main()
        main.run()
    except (Exception, KeyboardInterrupt) as e:
        print(e)
