from typing import Dict, List, Any
from parse_config import config_parsing
from Errors import InvalidEntryError, InvalidFileError

import os


def convert_to_int(val: str) -> bool:
    """Check if a string can be converted to an integer.

    Args:
        val (str): The string to check.

    Returns:
        bool: True if convertible to int, False otherwise.
    """
    try:
        int(val)
        return True
    except ValueError:
        return False


def validate(path: str) -> Dict[str, Any]:
    """Validate and parse the configuration file into typed values.

    Reads parsed config data, checks all mandatory keys exist,
    validates each value's type and range, and returns a typed
    configuration dictionary.

    Args:
        path (str): Path to the configuration file.

    Returns:
        Dict[str, Any]: Validated configuration with typed values.

    Raises:
        InvalidEntryError: If any key is missing, invalid, or out of bounds.
        InvalidFileError: If the output file has an invalid extension.
    """
    config: Dict[str, Any] = {}
    data: Dict[str, str] = config_parsing(path)

    VALID_ALGORITHMS: List[str] = [
        'recursive_backtracker', 'prim', 'kruskal', 'eller'
    ]
    MANDATORY_KEYS: List[str] = [
        'WIDTH', 'HEIGHT', 'ENTRY', 'EXIT', 'OUTPUT_FILE', 'PERFECT'
    ]

    for k in MANDATORY_KEYS:
        if k not in data:
            raise InvalidEntryError(
                f"Required configuration entry '{k}' is missing.")

    for k, v in data.items():

        if k in ('WIDTH', 'HEIGHT'):
            if not convert_to_int(v):
                raise InvalidEntryError(
                    f"Invalid number. Letters and special characters "
                    f"are not allowed for '{k}'.")
            config[k] = int(v)
            if config[k] <= 0:
                raise InvalidEntryError(f"'{k}' value must be 1 or higher.")

        elif k in ('ENTRY', 'EXIT'):
            coords: List[str] = v.split(',')
            if len(coords) != 2:
                raise InvalidEntryError(
                    f"Invalid '{k}': expected valid (x,y) coordinates.")

            x, y = coords
            if not convert_to_int(x) or not convert_to_int(y):
                raise InvalidEntryError(
                    f"'{k}' x,y coordinates must be integers.")

            config[k] = (int(x), int(y))

            valid_x: bool = 0 <= config[k][0] < config['WIDTH']
            valid_y: bool = 0 <= config[k][1] < config['HEIGHT']
            if not valid_x or not valid_y:
                raise InvalidEntryError(
                    f"'{k}' coordinates are out of bounds.")

        elif k == 'PERFECT':
            perfect: str = v.lower()
            if perfect not in ('true', 'false'):
                raise InvalidEntryError(
                    f"'{k}' must be 'True' or 'False'.")
            config[k] = perfect == 'true'

        elif k == 'OUTPUT_FILE':
            if not v:
                raise InvalidEntryError(
                    f"'{k}' must not be empty. "
                    f"Provide an output file (e.g. maze.txt).")
            _, ext = os.path.splitext(v)
            if ext != '.txt':
                raise InvalidFileError(
                    "Output file must be a plain text file (e.g. maze.txt).")
            config[k] = v

        elif k == 'SEED':
            if not v:
                continue
            if not convert_to_int(v):
                raise InvalidEntryError(
                    f"'{k}' must be a positive integer.")
            config[k] = int(v)
            if config[k] <= 0:
                raise InvalidEntryError(
                    f"'{k}' must be 1 or higher.")

        elif k == 'ALGORITHM':
            if not v:
                continue
            if v not in VALID_ALGORITHMS:
                raise InvalidEntryError(
                    f"'{k}' must be one of: "
                    f"{', '.join(VALID_ALGORITHMS)}.")
            config[k] = v

        else:
            raise InvalidEntryError(
                f"Configuration file has invalid key: '{k}'.")

    if config['ENTRY'] == config['EXIT']:
        raise InvalidEntryError(
            "ENTRY and EXIT coordinates must be different.")

    config.setdefault('SEED', None)
    config.setdefault('ALGORITHM', 'recursive_backtracker')

    return config
