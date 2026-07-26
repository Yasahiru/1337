*This project has been created as part of the 42 curriculum by <b>hloutman</b>.*

# Fly-in Drone Simulator

## Description
This project implements a drone route simulation engine that reads a map definition, validates the input format, finds candidate delivery paths, and executes turn-by-turn drone movement from a start hub to an end hub.

The goal is to model a constrained delivery environment where zones have capacity limits, connections have bandwidth constraints, and restricted zones require special movement handling.

## Instructions
1. Install dependencies:
   - Run `make install` to install required Python packages.
2. Execute the project:
   - Run `make run` or `python main.py <map-file>`.
   - Example: `python main.py maps/easy/01_linear_path.txt`
3. Debug:
   - Run `make debug` to start the project in Python's built-in debugger.
4. Clean:
   - Run `make clean` to remove generated caches and temporary files.

## Algorithm
The project follows a layered architecture:

- `parser.py` loads map files and validates format, zone metadata, and connections.
- `validator.py` constructs `Zone` and `Connection` objects from the parsed input.
- `graph_builder.py` builds a weighted graph representation from the zones and connections.
- `path_finder.py` searches for delivery paths between the start and end hubs and ranks them by cost.
- `simulator.py` runs the drone simulation, enforcing capacity and restricted-zone rules while moving drones turn by turn.

The simulation checks:

- whether a connection can accept another drone,
- whether a zone has room for incoming drones,
- how to handle delayed movement through restricted zones,
- when a drone reaches the end hub and is marked delivered.

## Visualization
The project includes a visual component using `pygame`.

- Zones are drawn as circles positioned according to their coordinates.
- Connections are drawn as lines between linked zones.
- Drones are displayed as moving markers on zones or midway along connections.

This visual representation makes it easier to understand the simulation state, verify route selection, and see how restrictions and capacities influence drone movement.

## Resources
- Python documentation: https://docs.python.org/3/
- Pygame documentation: https://www.pygame.org/docs/
- Mypy type checking: https://mypy.readthedocs.io/

### AI usage
AI assistance was used for:

- reviewing type annotations and `mypy` compatibility,
- helping create the `Makefile` automation rules,
- structuring this README and ensuring it met the required documentation sections.

AI was not used to implement the core simulation logic; it supported tooling, documentation, and code review only.
