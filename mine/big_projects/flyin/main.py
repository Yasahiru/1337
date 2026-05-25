from parser import Parser
from validator import Validator
import sys


def main() -> None:
    file_path = sys.argv[1]
    p = Parser(file_path)
    p.load()

    v = Validator()
    v.zones = p.zones
    v.conns = p.connections

    print(v.zones_obj())


if __name__ == "__main__":
    main()

# [
#     {
#         'name': 'start',
#         'x': 0,
#         'y': 0,
#         'meta_data': {'color': 'green'}
#     }, 
#     {
#         'name': 'waypoint1',
#         'x': 1,
#         'y': 0,
#         'meta_data': {'color': 'blue'}
#     }, 
#     {
#         'name': 'waypoint2',
#         'x': 2,
#         'y': 0,
#         'meta_data': {'color': 'blue'}
#         },
#     {
#         'name': 'goal',
#         'x': 3,
#         'y': 0,
#         'meta_data': {'color': 'red'}
#      }
# ]