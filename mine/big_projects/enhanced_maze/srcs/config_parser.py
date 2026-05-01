from typing import Tuple, Dict, Optional


class Config:
    """Handles configuration parsing and validation."""

    def __init__(self) -> None:
        self.width: int = 0
        self.height: int = 0
        self.entry: Tuple[int, int] = (0, 0)
        self.exit: Tuple[int, int] = (0, 0)
        self.output_file: str = ""
        self.perfect: bool = False
        self.seed: Optional[int] = None
        self.algo: str = ""

    def load(self, filename: str) -> None:
        """Load, parse, validate, and assign configuration."""
        lines = self._read_file(filename)
        data = self._parse(lines)
        self._validate_keys(data)
        self._assign(data)
        self._validate_logic()

    def _read_file(self, filename: str) -> list[str]:
        """Read file safely."""
        try:
            with open(filename, "r") as file:
                return file.readlines()
        except FileNotFoundError:
            raise ValueError(f"Config file not found: {filename}")

    def _parse(self, lines: list[str]) -> Dict[str, str]:
        """Parse lines into key-value pairs."""
        data: Dict[str, str] = {}

        for line in lines:
            line = line.strip()

            if not line or line.startswith("#"):
                continue

            key, value = self._parse_line(line)
            data[key] = value

        return data

    def _parse_line(self, line: str) -> Tuple[str, str]:
        """Split a line into key and value."""
        if "=" not in line:
            raise ValueError(f"Invalid line: {line}")

        if "#" in line:
            line = line.partition("#")[0]
        key, value = line.split("=")
        return key.strip().upper(), value.strip()

    def _validate_keys(self, data: Dict[str, str]) -> None:
        """Making sure all required keys exist."""
        required_keys = {
            "WIDTH", "HEIGHT", "ENTRY", "EXIT",
            "OUTPUT_FILE",
            "PERFECT"
        }

        bonus_keys = {
            "SEED",
            "ALGO",
        }

        # enhaced logic
        if not set(required_keys).issubset(data):
            missing = required_keys.difference(data)
            raise ValueError(f"Missing key{'s' if len(missing) > 1 else ''}: {', '.join(missing)}")

        for key in data:
            if key not in (*bonus_keys, *required_keys):
                raise ValueError(f"Uknown key: {key}")

    def _assign(self, data: Dict[str, str]) -> None:
        """Convert and assign values."""
        try:
            self.width = int(data["WIDTH"])
            self.height = int(data["HEIGHT"])
            self.entry = self._parse_coordinates(data["ENTRY"])
            self.exit = self._parse_coordinates(data["EXIT"])
            self.output_file = data["OUTPUT_FILE"]
            self.perfect = self._parse_bool(data["PERFECT"])
            try:
                algo = data["ALGO"].strip().upper()
            except Exception:
                algo = "DFS"
            self.algo = algo

            # remove int()
            if "SEED" in data:
                self.seed = data["SEED"]
            else:
                self.seed = None
        except ValueError as e:
            raise ValueError(f"Invalid value: {e}")

    def _parse_coordinates(self, value: str) -> Tuple[int, int]:
        """Parse 'x,y' into (x, y)."""
        try:
            x, y = value.split(",")
            return int(x), int(y)
        except (ValueError, IndexError):
            raise ValueError(f"Invalid coordinates: {value}")

    def _parse_bool(self, value: str) -> bool:
        """Parse boolean values."""
        value = value.lower()

        if value in ("true", "1", "yes"):
            return True
        if value in ("false", "0", "no"):
            return False

        raise ValueError(f"Invalid boolean: {value}")

    def _validate_logic(self) -> None:
        """Validate logical correctness."""

        if self.width <= 0 or self.height <= 0:
            raise ValueError("Width and Height must be positive")

        if self.entry == self.exit:
            raise ValueError("Entry and Exit cannot be the same")

        if not self._in_bounds(self.entry):
            raise ValueError("Entry out of bounds")

        if not self._in_bounds(self.exit):
            raise ValueError("Exit out of bounds")

    def _in_bounds(self, coord: Tuple[int, int]) -> bool:
        """Check if coordinates are inside maze."""
        x, y = coord
        return 0 <= x < self.width and 0 <= y < self.height
