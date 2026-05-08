from typing import Dict, List
# import re
# //


class Parser:
    def __init__(self, file_path) -> None:
        self.file_path: str = file_path
        self.nb_drones: int = 0
        self.cleared_zones: Dict[str, str] = {}
        self.cleared_connections: Dict[str, str] = {}
        self.available_zones = []

    def load(self) -> None:
        try:
            zones = []
            connections = []
            content = self._read_file(self.file_path)
            for line in content:
                if line.startswith(("hub", "start_hub", "end_hub")):
                    zones.append(line)
                elif line.startswith("connection"):
                    connections.append(line)
            self.cleared_zones = self.parse_zones(zones)
            self.cleared_connections = self.parse_connections(connections)
        except KeyboardInterrupt as e:
            print(e)

    def _read_file(self, filename: str) -> List[str]:
        content = []
        with open(filename, "r") as f:
            for line in f:
                if line.startswith("#") or line == "\n":
                    continue
                else:
                    content.append(line)

        if content[0].startswith("nb_drones"):
            self.nb_drones = int(content[0].split(":")[1])
        else:
            raise ValueError("nb_drones Should be at the top of the file!!")
        return content

    def parse_zones(self, zones: List[str]) -> Dict[str, List[str]]:
        filtered_zones = {}
        c = 0
        for z in zones:
            if z.startswith("start_hub:"):
                zone_info = (z.split(":")[1]).strip()
                val = self.clear_zone(zone_info)
                filtered_zones["start_hub"] = val
                self.available_zones.append(val["name"])
            elif z.startswith("end_hub:"):
                zone_info = (z.split(":")[1]).strip()
                val = self.clear_zone(zone_info)
                filtered_zones["end_hub"] = val
                self.available_zones.append(val["name"])
            elif z.startswith("hub:"):
                c += 1
                zone_info = (z.split(":")[1]).strip()
                val = self.clear_zone(zone_info)
                filtered_zones[f"hub{c}"] = val
                self.available_zones.append(val["name"])
        return (filtered_zones)

    def clear_zone(self, zone: str) -> Dict[str, str]:
        inp = zone.split(" ")
        res = {
            "name": inp[0],
            "x": int(inp[1]),
            "y": int(inp[2]),
            "meta_data": {}
        }
        if len(inp) > 3:
            s = zone.rfind("[")
            e = zone.rfind("]") + 1
            sep = zone[s:e]
            if (len(sep) != 1):
                sep = sep.replace("[", "")
                sep = sep.replace("]", "")
                sep.strip()
                meta_data = sep.split(" ")
                for data in meta_data:
                    d = data.split("=")
                    res["meta_data"].update({d[0]: d[1]})
        return res

    def parse_connections(self, conn: List[str]) -> Dict[str, List[str]]:
        filtered_conns = []
        cleared_conn = []
        for line in conn:
            cleared_conn.append(line.split(":")[1])
        cleared_conn = list(map(lambda s: s.strip(), cleared_conn))
        for c in cleared_conn:
            zones = c.split("-")
            meta_data = []
            if zones[1].find("[") != -1 and zones[1].find("]") != -1:
                meta_data = zones[1].split("[")[1].replace("]", "").strip()
                zones[1] = zones[1].split("[")[0].strip()
            filtered_conns.append({
                "zone1": zones[0],
                "zone2": zones[1],
                "meta_data": meta_data
            })
            for _ in filtered_conns:
                for k, v in _.items():
                    if k == "zone1":
                        if v not in self.available_zones:
                            raise ValueError("test")
                    elif k == "zone2":
                        if v not in self.available_zones:
                            raise ValueError("test")
        return (filtered_conns)

    def find_error_file():
        ...


try:
    t = Parser("conf.txt")
    t.load()

    print("zones")
    for key, val in t.cleared_zones.items():
        print(key, ":")
        for k, v in val.items():
            print("\t", end="")
            print(k, v, sep=" : ")
    print()

    print("connections")
    for _ in t.cleared_connections:
        for k, v in _.items():
            print(k, v, sep=" : ", end="\t")
        print()

    print()
    print("available zones: ", t.available_zones)
except KeyboardInterrupt as e:
    print(e)


# # re.match(r"^connection:\s+[^- ]-[^- ]\s+([.*])?$")
# print(re.search(r"^hub:\s+[^- ]+\s+\d+\s+\d+\s+(\[.*\])?$", "hub: A1 2 1 [color=blue]"))
