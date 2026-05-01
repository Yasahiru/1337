from typing import Dict, List


class Cell:
    """Represent a single cell in a maze grid.

    Each cell tracks its position, the state of its four walls,
    and whether it has been visited during maze generation.

    Attributes:
        x (int): The horizontal position of the cell in the grid.
        y (int): The vertical position of the cell in the grid.
        walls (Dict[str, bool]): Wall states keyed by direction
            ('N', 'E', 'S', 'W'). True means open, False means closed.
        visited (bool): Whether this cell has been visited
            during maze generation.
    """

    def __init__(self, x: int, y: int) -> None:
        """Initialize a Cell at position (x, y) with all walls closed.

        Args:
            x (int): The horizontal position of the cell.
            y (int): The vertical position of the cell.
        """
        self.x: int = x
        self.y: int = y
        self.walls: Dict[str, bool] = {
            "N": False,
            "E": False,
            "S": False,
            "W": False,
        }
        self.visited: bool = False

    def to_hex(self) -> str:
        """Encode the cell's wall states as a single hexadecimal character.

        Each wall maps to a bit position:
            - North: bit 0 (LSB)
            - East:  bit 1
            - South: bit 2
            - West:  bit 3 (MSB)

        A closed wall (False) sets its bit to 1;
        an open wall (True) sets it to 0.

        Returns:
            str: A single uppercase hex character (e.g., 'F', '3', 'A')
                representing the wall configuration of the cell.

        Example:
            A cell with only North and East closed returns '3' (binary 0011).
        """
        HEX: str = "0123456789ABCDEF"
        BIT_INDEX: Dict[str, int] = {"N": 0, "E": 1, "S": 2, "W": 3}
        wall: List[str] = ["1", "1", "1", "1"]

        for key, i in BIT_INDEX.items():
            if self.walls[key]:
                wall[i] = "0"

        return HEX[int("".join(reversed(wall)), 2)]
