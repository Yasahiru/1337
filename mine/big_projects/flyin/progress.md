<h2> Task1: </h2>    

<pre>
def build_graph(self, zones, conns) -> dict:
        for zone in zones:
            self.graph[zone.name] = []

            for conn in conns:
                if conn.zone1 == zone.name:
                    weight = self.get_zone_cost(zone)
                    if weight < 0:
                        continue
                    self.graph[zone.name].append((conn.zone2, weight))
                elif conn.zone2 == zone.name:
                    weight = self.get_zone_cost(zone)
                    if weight < 0:
                        continue
                    self.graph[zone.name].append((conn.zone1, weight))
        return self.graph
</pre>

<h2> Result: </h2>

<code>
    base: [('A1', 1)]
    target: [('D4', 1), ('F6', 1)]
    A1: [('base', 1), ('B2', 1), ('E5', 1)]
    B2: [('A1', 2), ('C3', 2)]
    C3: [('B2', 1), ('D4', 1)]
    D4: [('C3', 1), ('target', 1)]
    E5: []
    F6: [('E5', 1), ('target', 1)]
</code>


<h2> Task2 + Task3 (djikstra.py)</h2>

<pre>
class Algo:

    def __init__(self, zones, graph) -> None:
        self.zones = zones
        self.graph = graph
        self.distances = {}
        self.previous = {}
        self.unvisited = set()

    def load(self, start: str) -> None:
        for z in self.zones:
            self.distances[z.name] = float("inf")
            self.previous[z.name] = None
        self.distances[start] = 0
        self.unvisited = set(self.graph.keys())
</pre>


<h2> Test</h2>
<code>
    algo = Algo(zones, graph)
    res = algo.load("base")
    dis = algo.distances
</code>

<h2> Result</h2>

<code>
    base: 0
    target: inf
    A1: inf
    B2: inf
    C3: inf
    D4: inf
    E5: inf
    F6: inf
</code>