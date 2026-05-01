*This project has been created as part of the 42 curriculum by <maderrab>, <hloutman>*

## Description

**A-Maze-ing** is a Python-based maze generator that creates valid and structured mazes using algorithmic logic and randomness.

The goal of this project is to explore **random generation** and **algorithm design** by implementing a system capable of:
- Generating mazes based on a configuration file
- Ensuring structural validity
- Exporting the maze using a hexadecimal wall encoding
- Displaying the maze visually (terminal)
- Providing the shortest path from entry to exit

A key concept behind this project is the generation of **perfect mazes**, where there exists exactly **one unique path** between any two cells, and **imperfect mazes**, where multiple paths may exist.

---

## Instructions

### Installation

Clone the repository and install the required dependencies:

```bash
git clone <your-repo-url>
cd a-maze-ing
make install
```

Alternatively, install dependencies manually:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Execution

Run the program with a configuration file:

```bash
python3 a_maze_ing.py config.txt
```

Or using the Makefile:

```bash
make run
```

### Debug Mode

Run the program using Python's debugger:

```bash
make debug
```

### Linting & Type Checking

Check code quality and type safety:

```bash
make lint
```

Optional strict mode:

```bash
make lint-strict
```

### Cleaning

Remove temporary files and caches:

```bash
make clean
```

---

## Resources

### Documentation and References

- https://en.wikipedia.org/wiki/Maze_generation_algorithm
- https://en.wikipedia.org/wiki/Depth-first_search
- https://realpython.com/python-maze-solver/


These resources were used to understand maze generation techniques and Python implementation details.

---

## AI Usage

AI tools (such as ChatGPT) were used during this project to assist with:
- Understanding maze generation algorithms (e.g., recursive backtracking, graph concepts)
- Structuring the project and organizing modules
- Debugging specific issues and improving code clarity
- Generating and refining documentation (including this README)

All AI-generated content was:
- Carefully reviewed
- Fully understood before integration
- Tested within the project context

AI was used as a support tool to improve productivity and learning, not as a replacement for problem-solving. All core logic and implementation decisions were validated and adapted manually.

## Configuration File

The configuration file defines all parameters required to generate the maze. It follows a simple `KEY=VALUE` format, one entry per line.

### Example

WIDTH=15
HEIGHT=15
ENTRY=0,0
EXIT=14,14
OUTPUT_FILE=maze.txt
SEED=0
ALGO=prim
PERFECT=1


### Format Rules

- Each line must follow the format: `KEY=VALUE`
- Empty lines are ignored
- Lines starting with `#` are treated as comments
- Coordinates are defined as `x,y` without spaces
- The seed is optional and used for reproducibility
- `PERFECT=1` means the maze must have a unique solution


## Maze Generation Algorithm

Two algorithms were explored during the project:

- **Depth-First Search (DFS) / Recursive Backtracking**
- **Prim's Algorithm**


We chose the DFS (recursive backtracking) algorithm because it is simple to implement and debug while still being powerful enough to generate high-quality mazes. It naturally produces perfect mazes by ensuring there is exactly one unique path between any two cells, and it guarantees full connectivity across the entire grid.

Prim’s algorithm was also explored during development for learning purposes and to understand alternative approaches to maze generation, as well as to compare different generation styles and their resulting maze structures.


---

## Code Reusability

The reusable component of the project is the `MazeGenerator` class.

### Features

- Independent from input/output logic
- Can generate mazes of any size
- Supports multiple algorithms (DFS, Prim)
- Exposes internal maze structure for external use
- Provides solution path computation

The module is designed to be imported as a standalone library in future projects.

---

## Team & Project Management

### Roles

| Member | Responsibilities |
|--------|-----------------|
| maderrab | Parsing system, configuration handling, and algorithm implementation |
| hloutman | Output generation, visualization, and display logic |

### Planning and Evolution

**Initial Plan:**
- Implement the config parser
- Implement the maze generator
- Generate the output file
- Display the maze in the terminal

**How the project evolved:**
- Added multiple algorithms (DFS and Prim) for flexibility
- Improved error handling and input validation
- Refactored core logic into a reusable `MazeGenerator` class
- Enhanced output formatting and overall code structure

## What Worked Well and What Could Be Improved

The collaboration between team members worked well, with a clear separation of responsibilities that allowed each part of the project to progress efficiently. Regular communication helped ensure consistency between the parsing, generation, and display components of the project. The use of AI tools also helped accelerate problem-solving, improve documentation quality, and clarify complex concepts during development.

However, time management could have been improved. Better planning and earlier task distribution would have helped reduce last-minute integration and allowed more time for testing and refinement of edge cases.

---

## Tools Used

Several tools were used throughout the project to support development and ensure code quality:

- Python 3.10+ for implementation
- Git and GitHub for version control and collaboration
- flake8 for code style checking and linting
- mypy for static type checking
- pytest (optional) for testing and validation
- AI tools (ChatGPT) for assistance with:
  - Understanding maze generation algorithms
  - Debugging and explaining issues
  - Improving documentation and README structure
  - Clarifying design decisions and best practices