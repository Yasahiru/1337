class InvalidConfigError(Exception):
    """Base exception for all configuration-related errors."""
    pass


class InvalidEntryError(InvalidConfigError):
    """Raised when the configuration file has an invalid entry."""
    pass


class InvalidFileError(InvalidConfigError):
    """Raised when the configuration file is missing or unreadable."""
    pass


class InvalidArgumentError(InvalidConfigError):
    """Raised when a configuration key has an invalid or missing value."""
    pass
