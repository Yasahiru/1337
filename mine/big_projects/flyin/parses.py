from typing import Dict, List
import sys


class Parser:
    def __init__(self, file_path):
        self.file_path: str = file_path
        self.nb_drones: int = 0
        self.cleared_zones: Dict[str, str] = {}
        self.cleared_connections: Dict[str, str] = {}

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
        except KeyboardInterrupt as e:
            print(e)

    def _read_file(self, filename: str) -> None:
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

        for z in zones:
            if z.startswith("start_hub"):
                zone_info = (z.split(":")[1]).strip()
                val = self.clear_zone(zone_info)
                filtered_zones["start_hub"] = val
            elif z.startswith("end_hub"):
                zone_info = (z.split(":")[1]).strip()
                val = self.clear_zone(zone_info)
                filtered_zones["end_hub"] = val
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


t = Parser("conf.txt")
t.load()
