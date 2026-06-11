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







Yes, that's a much better direction.

Keep the pathfinding logic separate from `Validator`.

Something like:

```text
model/
parser/
simulation/
    algo.py
```

is clean.

---

I'd slightly change your class:

```python
class Algo:

    def __init__(self, zones, graph):
        self.zones = zones
        self.graph = graph

        self.distances = {}
        self.previous = {}
        self.unvisited = set()
```

You probably don't need `conns` anymore once the graph is built.

---

Your `load()` should initialize all Dijkstra structures:

```python
def load(self, start):
    for zone in self.zones:
        self.distances[zone.name] = float("inf")

    self.distances[start] = 0

    self.unvisited = set(self.graph.keys())
```

Then test:

```python
algo = Algo(zones, graph)

algo.load("base")

print(algo.distances)
print(algo.unvisited)
```

Expected:

```python
{
    "base": 0,
    "A1": inf,
    "B2": inf,
    ...
}
```

and

```python
{
    "base",
    "A1",
    "B2",
    ...
}
```

---

### After that

Create a method:

```python
def get_current_node(self):
```

whose job is:

```python
return min(
    self.unvisited,
    key=lambda node: self.distances[node]
)
```

Test:

```python
print(algo.get_current_node())
```

Expected:

```text
base
```

because:

```python
base = 0
everything else = inf
```

---

### Then

Create another method:

```python
def get_neighbors(self, node):
    return self.graph[node]
```

Test:

```python
print(algo.get_neighbors("A1"))
```

Expected:

```python
["base", "B2", "E5"]
```

---

Once these three methods work:

```python
load()
get_current_node()
get_neighbors()
```

you're ready to write the main Dijkstra loop:

```python
while self.unvisited:
    current = self.get_current_node()

    ...
```

Don't jump directly into the full algorithm. Build and test these small pieces first. It will save you a lot of debugging later.
