

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
