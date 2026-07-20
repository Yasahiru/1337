from __future__ import annotations
from typing import Any, Dict, List, Tuple, Set
import re


class Parser:
    z_pattern = r"^(start_hub|end_hub|hub):\s+([^\s\-]+)\s+(-?\d+)"
    z_pattern += r"\s+(-?\d+)(?:\s+\[(.*)\])?$"
    ZONE_LINE_PATTERN = re.compile(z_pattern)

    conn_patt: str = r"^connection:\s+([^\s\-]+)-([^\s\-]+)(?:\s+\[(.*)\])?$"
    CONNECTION_LINE_PATTERN = re.compile(conn_patt)

    ALLOWED_ZONE_TYPES: Set[str] = {
        "normal", "blocked", "restricted", "priority"
    }
    ALLOWED_ZONE_METADATA: Set[str] = {
        "zone", "color", "max_drones", "zone_role"
    }
    ALLOWED_CONNECTION_METADATA: Set[str] = {"max_link_capacity"}

    def __init__(self, file_path: str) -> None:
        self.file_path: str = file_path
        self.nb_drones: int = 0
        self.zones: List[Dict[str, Any]] = []
        self.connections: List[Dict[str, Any]] = []
        self.coords: List[Tuple[int, int]] = []
        self._zone_names: Set[str] = set()
        self._connection_pairs: set[frozenset[str]] = set()

    def load(self) -> None:
        content = self._read_file(self.file_path)

        for line_number, line in content:
            stripped = line.strip()
            if "#" in stripped:
                _line = stripped.split("#")[0].strip()
            else:
                _line = stripped

            if stripped.startswith(("hub:", "start_hub:", "end_hub:")):
                self.parse_zone(line_number, _line)
            elif stripped.startswith("connection:"):
                self.parse_connection(line_number, _line)
            else:
                raise ValueError(
                    f"Error in line {line_number}: unsupported line format"
                )

        self._validate_zones()

    def _read_file(self, filename: str) -> List[tuple[int, str]]:
        content: List[tuple[int, str]] = []
        with open(filename, "r", encoding="utf-8") as f:
            for index, raw_line in enumerate(f, start=1):
                line = raw_line.rstrip("\n")
                stripped = line.strip()
                if not stripped or stripped.startswith("#"):
                    continue
                content.append((index, line))

        if not content:
            raise ValueError("Error: input file is empty")

        first_line = content[0][1].strip()
        if not first_line.lower().startswith("nb_drones:"):
            line_number = content[0][0]
            raise ValueError(
                f"Error in line {line_number}: first line must be"
                " 'nb_drones: <positive_integer>'"
            )

        _, value = first_line.split(":", 1)
        try:
            self.nb_drones = int(value.strip())
        except ValueError:
            raise ValueError(
                f"Error in line {content[0][0]}: "
                "nb_drones must be a positive integer"
            )

        if self.nb_drones <= 0:
            raise ValueError(
                f"Error in line {content[0][0]}: "
                "nb_drones must be greater than zero"
            )

        return content[1:]

    def parse_zone(self, line_number: int, line: str) -> None:
        match = self.ZONE_LINE_PATTERN.match(line)
        if not match:
            raise ValueError(
                f"Error in line {line_number}: invalid zone syntax"
            )

        prefix, name, x_str, y_str, metadata_str = match.groups()
        if "-" in name or " " in name:
            raise ValueError(
                f"Error in line {line_number}: invalid zone name '{name}'"
            )
        if name in self._zone_names:
            raise ValueError(
                f"Error in line {line_number}: duplicate zone name '{name}'"
            )

        x = int(x_str)
        y = int(y_str)
        metadata = self._parse_metadata(
            line_number, metadata_str, self.ALLOWED_ZONE_METADATA
        )

        zone_type = metadata.get("zone", "normal")
        if zone_type not in self.ALLOWED_ZONE_TYPES:
            raise ValueError(
                f"Error in line {line_number}: invalid zone type '{zone_type}'"
            )

        self._parse_positive_int(
            line_number,
            metadata.get("max_drones"),
            "max_drones",
            default=1,
        )

        coords = (x, y)
        if self.is_coords_exist(coords):
            raise ValueError(
                f"Error in line {line_number}: "
                f"Duplication in zone ({name}) coordinates '{coords}'"
            )
        self.coords.append(coords)
        self.zones.append(
            {
                "kind": prefix,
                "name": name,
                "x": x,
                "y": y,
                "meta_data": metadata,
            }
        )
        self._zone_names.add(name)

    def is_coords_exist(self, coords: Tuple[int, int]) -> bool:
        for coord in self.coords:
            if coord == coords:
                return True
        return False

    def parse_connection(self, line_number: int, line: str) -> None:
        match = self.CONNECTION_LINE_PATTERN.match(line)
        if not match:
            raise ValueError(
                f"Error in line {line_number}: invalid connection syntax"
            )

        zone1, zone2, metadata_str = match.groups()
        if zone1 not in self._zone_names:
            raise ValueError(
                f"Error in line {line_number}: unknown zone '{zone1}'"
            )
        if zone2 not in self._zone_names:
            raise ValueError(
                f"Error in line {line_number}: "
                f"unknown zone '{zone2}'"
            )
        if zone1 == zone2:
            raise ValueError(
                f"Error in line {line_number}: "
                "connection must link two different zones"
            )

        connection_key = frozenset({zone1, zone2})
        if connection_key in self._connection_pairs:
            raise ValueError(
                f"Error in line {line_number}: duplicate connection "
                f"between '{zone1}' and '{zone2}'"
            )

        metadata = self._parse_metadata(
            line_number, metadata_str, self.ALLOWED_CONNECTION_METADATA
        )

        self._parse_positive_int(
            line_number,
            metadata.get("max_link_capacity"),
            "max_link_capacity",
            default=1,
        )

        self.connections.append(
            {
                "zone1": zone1,
                "zone2": zone2,
                "meta_data": metadata,
            }
        )
        self._connection_pairs.add(connection_key)

    def _parse_metadata(
        self,
        line_number: int,
        metadata_str: str | None,
        allowed_keys: set[str],
    ) -> Dict[str, str]:
        metadata: Dict[str, str] = {}
        if not metadata_str:
            return metadata

        for token in metadata_str.split():
            if "=" not in token:
                raise ValueError(
                    f"Error in line {line_number}: "
                    f"invalid metadata token '{token}'"
                )
            key, value = token.split("=", 1)
            if key not in allowed_keys:
                raise ValueError(
                    f"Error in line {line_number}: invalid "
                    f"metadata key '{key}'"
                )
            if not value:
                raise ValueError(
                    f"Error in line {line_number}: metadata '{key}' "
                    "must have a value"
                )
            if key == "max_drones":
                self._parse_positive_int(line_number, value, key)
            metadata[key] = value

        return metadata

    def _parse_positive_int(
        self,
        line_number: int,
        value: str | None,
        field_name: str,
        default: int = 1,
    ) -> int:
        if value is None:
            return default
        try:
            parsed_value = int(value)
        except ValueError:
            raise ValueError(
                f"Error in line {line_number}: "
                f"{field_name} must be a positive integer"
            )
        if parsed_value <= 0:
            raise ValueError(
                f"Error in line {line_number}: "
                f"{field_name} must be a positive integer"
            )
        return parsed_value

    def _validate_zones(self) -> None:
        start_count = sum(
            1 for zone in self.zones if zone["kind"] == "start_hub"
        )
        end_count = sum(1 for zone in self.zones if zone["kind"] == "end_hub")

        if start_count != 1:
            raise ValueError(
                f"Error: expected exactly one start_hub, found {start_count}"
            )
        if end_count != 1:
            raise ValueError(
                f"Error: expected exactly one end_hub, found {end_count}"
            )
