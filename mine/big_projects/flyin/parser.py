from typing import Dict, List
import re


class Parser:
    def __init__(self, file_path) -> None:
        self.file_path: str = file_path
        self.nb_drones: int = 0
        self.available_zones = []

        self.zones: List[str] = []
        self.connections: List[str] = []

    def load(self) -> None:
        try:
            content = self._read_file(self.file_path)

            for line in content:
                if line[1].startswith(("hub", "start", "end")):
                    self.parse_zone(line)
                elif line[1].startswith("connection"):
                    self.parse_connections(line)

        except KeyboardInterrupt as e:
            print(e)

    def _read_file(self, filename: str) -> List[str]:
        zones = []
        connections = []
        content = []
        with open(filename, "r") as f:
            for index, line in enumerate(f, start=1):
                if line.startswith("#") or line == "\n":
                    continue
                else:
                    content.append((index, line))
                if line.startswith("connection"):
                    connections.append(line)
                    if not self.check_duplication(connections):
                        raise ValueError(
                            f"Duplication in line: {index} {line}"
                        )
                if line.startswith(("hub", "start_hub", "end_hub")):
                    zones.append(line)
                    if len(zones) != len(set(zones)):
                        raise ValueError(f"Duplication in line: {index}")

        if content[0][1].startswith("nb_drones"):
            self.nb_drones = int(content[0][1].split(":")[1])
            content.reverse()
            content.pop()
            content.reverse()
        else:
            raise ValueError(
                f"Error in line {content[0][0]}: "
                "nb_drones Should be at the top of the file!!"
                )

        return content

    def parse_zone(self, z: tuple[int, str]) -> None:
        reg = r"^(hub|start_hub|end_hub):\s+[^- ]+\s+\d+\s+\d+\s+(\[.*\])?$"
        if not re.match(reg, z[1]):
            raise ValueError(f"Error in line {z[0]}: {z[1]}")

        if z[1].startswith("start_hub:"):
            zone_info = (z[1].split(":")[1]).strip()
            val = self.clear_zone(zone_info)
            self.available_zones.append(val["name"])
            self.zones.append(val)
        elif z[1].startswith("end_hub:"):
            zone_info = (z[1].split(":")[1]).strip()
            val = self.clear_zone(zone_info)
            self.available_zones.append(val["name"])
            self.zones.append(val)
        elif z[1].startswith("hub:"):
            zone_info = (z[1].split(":")[1]).strip()
            val = self.clear_zone(zone_info)
            self.available_zones.append(val["name"])
            self.zones.append(val)

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

    def parse_connections(self, conn: str) -> None:
        cleared_conn = (conn[1].split(":")[1].strip())
        zones = cleared_conn.split("-")
        meta_data = []

        if zones[1].find("[") != -1 and zones[1].find("]") != -1:
            meta_data = zones[1].split("[")[1].replace("]", "").strip()
            zones[1] = zones[1].split("[")[0].strip()

        if zones[0] not in self.available_zones:
            raise ValueError(f"Uknown zone in line: {conn[0]}")
        if zones[1] not in self.available_zones:
            raise ValueError(f"Uknown Zone Name in line: {conn[0]}")

        self.connections.append({
            "zone1": zones[0],
            "zone2": zones[1],
            "meta_data": meta_data
        })

    def check_duplication(self, lst: List[str]) -> bool:
        seen = []
        for _ in lst:
            sor = sorted(_)
            if sor not in seen:
                seen.append(sor)
            else:
                return False
        return True
