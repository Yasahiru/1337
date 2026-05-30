*This project has been created as part of the 42 curriculum by <hloutman>.

# Fly-in Drone Simulator

## Description
This project parses drone map files, validates the input format, and simulates multiple drones moving from a start hub to an end hub.

## Current state
- Parser and map validator are implemented and enforce the required format.
- A basic simulation engine is implemented with turn-by-turn drone movement.
- The simulator handles zone capacities, connection capacities, and restricted-zone 2-turn movement.

## Progress
- **Current completion: 65%**
- Completed:
  - Input parsing and validation
  - Zone and connection models
  - Basic simulation engine and move output
  - Multi-path allocation for drone dispatch
- Next step:
  - Add visual terminal output
  - Add tests, linting, and README cleanup

## How to run
```bash
python main.py maps/easy/01_linear_path.txt
```

## Notes
- The project is written in Python 3.10+.
- The next focus is on simulation quality and report formatting.
