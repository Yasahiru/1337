from typing import Dict, List


class Parser:
    def __init__(self, file_path):
        self.file_path: str = file_path
        self.nb_drones: int = 0
        self.zones: List[str] = []
        self.connections: List[str] = []

    def load(self) -> None:
        try:
            self._read_file(self.file_path)
            # self.parse_zones(self.zones)
        except Exception as e:
            print(e)

    def _read_file(self, filename: str) -> None:
        content = []
        with open(filename, "r") as f:
            for line in f:
                if line.startswith("#"):
                    continue
                else:
                    content.append(line)

        if content[0].startswith("nb_drones"):
            self.nb_drones = int(content[0].split(":")[1])
        else:
            raise ValueError("nb_drones Should be at the top of the file!!")

        for line in content:
            if line.startswith(("hub", "start_hub", "end_hub")):
                self.zones.append(line)
            elif line.startswith("connection"):
                self.connections.append(line)

    def _parse(self, lines: list[str]) -> Dict[str, str]:
        ...

    def parse_zones(self) -> Dict[str, List[str]]:
        filtered_zones = {}

        for z in self.zones:
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
        # ['base', '0', '0', '[color=green]']
        res = {
            "name": inp[0],
            "x": int(inp[1]),
            "y": int(inp[2]),
            "meta_data": None
        }

        # import sys
        # sys.exit()

        if len(inp) > 3:
            sep = zone.split("[")
            if (len(sep) != 1):
                meta_data = zone.replace(sep[0], "")
                meta_data.strip()
                meta_data = meta_data.replace("[", "")
                meta_data = meta_data.replace("]", "")
                meta_data = meta_data.split(" ")

                for data in meta_data:
                    d = data.split("=")
                    res["meta_data"].update({d[0]: d[1]})

        return res


t = Parser("conf.txt")
t.load()
_dict = t.parse_zones()

for key, val in _dict.items():
    print(key, ":")
    for k, v in val.items():
        print("\t", end="")
        print(k, v, sep=" : ")
    print()

# test = {
#     "1": {
#         "a": "b"
#     }
# }

# test["1"].update({"c": "d"})
# print(test)

# v = "base 0 0 [color=green zone=test]"

# print(
#     v[:v.rfind("[")]
# )

# print(
#     t.nb_drones,
# )

# for _ in t.zones:
#     print(_, end="")
# print()

# for _ in t.connections:
#     print(_, end="")
