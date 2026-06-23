import sys
from parser.parser import Parser
from parser.validator import Validator
from simulation.path_finder import PathFinder
from simulation.simulator import Simulator


def main():
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

    logs = sim.run()

    for d in sim.drones:
        print(d.drone_id, end=": ")
        for t in d.assigned_path:
            print(t.name, end=" ")
        print()

    print()
    for log in logs:
        print(log)

    # debug
    # d = sim.drones[2]
    # print(d.assigned_path[0].name, d.assigned_path[1].name)
    # nxt = sim.get_next_zone(d)

    # con = sim.find_connection(d.current_location, nxt)
    # print("con: ", con)

    # can = sim.can_drone_move(d)
    # print(can)

    # sim.move_normal_drone(d, nxt)
    # print(nxt.name, d.current_location.name)

    # sim.update_transit_drones()
    # print(d.path_index)

    # print(sim.find_connection(d.current_drones, nextz))
    # for log in logs:
    #     print(log)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt as e:
        print(e)

    # from model.zone import Zone
    # from model.connection import Connection
    # from model.drone import Drone

    # z1 = Zone(name="Z1", x=0, y=0, max_drones=2)
    # z2 = Zone(name="Z2", x=1, y=1, max_drones=2)
    # c = Connection(z1, z2, f"{z1}-{z2}", 2)
    # conns = [c]

    # d = Drone("D1", ["Z1", "Z2", ], z1)
    # res = sim.find_connection(d.current_location, z2)
    # print(res)
