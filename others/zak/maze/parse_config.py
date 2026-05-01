from typing import Dict, List
from Errors import InvalidEntryError, InvalidFileError


def config_parsing(path: str) -> Dict[str, str]:
    """Parse a configuration file into a dictionary of key-value pairs.

    Reads a plain text file containing KEY=VALUE pairs, ignoring
    blank lines and lines starting with '#'.

    Args:
        path (str): Path to the configuration file.

    Returns:
        Dict[str, str]: Parsed configuration data as a dictionary.

    Raises:
        InvalidEntryError: If a line has an empty value or invalid format.
        InvalidFileError: If the file is not found or cannot be read.
    """
    try:
        with open(path, "r") as file:
            config: Dict[str, str] = {}

            for line in file:
                clean_line: str = line.strip()

                if not clean_line or clean_line.startswith("#"):
                    continue

                item: List[str] = clean_line.split('=')
                if len(item) != 2 or item[1] == '':
                    raise InvalidEntryError(
                        f"This entry '{item[0]}' cannot be empty.")

                k, v = item
                config[k] = v

        return config

    except FileNotFoundError:
        raise InvalidFileError(f"'{path}' configuration file does not exist.")
    except OSError as e:
        raise InvalidFileError(f"Unexpected file error: {e}")
