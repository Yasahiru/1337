

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

    def get_min_unvisited(self) -> str:
        mine_zone = None
        min_dist = float("inf")

        for z in self.unvisited:
            if self.distances[z] < min_dist:
                min_dist = self.distances[z]
                mine_zone = z
        return mine_zone

    def relax(self, current) -> None:
        cur = self.graph[current]
        for el in cur:
            neigh = el[0]
            dest = el[1]
            new_dest = self.distances[current] + dest
            if new_dest < self.distances[neigh]:
                self.distances[neigh] = new_dest
                self.previous[neigh] = current

    def run(self, start) -> None:
        self.load(start)
        while self.unvisited:
            current = self.get_min_unvisited()
            if current is None or self.distances[current] == float("inf"):
                break
            self.relax(current)
            self.unvisited.remove(current)
