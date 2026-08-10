from typing import Tuple


RGB_COLORS: dict[str, tuple[int, int, int]] = {
    # Standard colors
    "black": (0, 0, 0),
    "red": (255, 0, 0),
    "green": (0, 128, 0),
    "yellow": (255, 255, 0),
    "blue": (0, 0, 255),
    "magenta": (255, 0, 255),
    "cyan": (0, 255, 255),
    "white": (255, 255, 255),
    # Bright colors
    "gray": (128, 128, 128),
    "light_red": (255, 102, 102),
    "light_green": (144, 238, 144),
    "light_yellow": (255, 255, 153),
    "light_blue": (173, 216, 230),
    "light_magenta": (255, 153, 255),
    "light_cyan": (224, 255, 255),
    # Extra colors
    "orange": (255, 165, 0),
    "purple": (128, 0, 128),
    "brown": (139, 69, 19),
    "maroon": (128, 0, 0),
    "gold": (255, 215, 0),
    "darkred": (139, 0, 0),
    "crimson": (220, 20, 60),
    "violet": (238, 130, 238),
    # Common extras
    "pink": (255, 192, 203),
    "navy": (0, 0, 128),
    "teal": (0, 128, 128),
    "lime": (50, 205, 50),
    "olive": (128, 128, 0),
    "turquoise": (64, 224, 208),
    "indigo": (75, 0, 130),
    "coral": (255, 127, 80),
    "salmon": (250, 128, 114),
    "beige": (245, 245, 220),
    "silver": (192, 192, 192),
    "aqua": (0, 255, 255),
    # Special/fun
    "rainbow": (0, 255, 255),  # same as aqua/cyan
}

DEFAULT_COLOR = (255, 255, 255)  # white


def get_color(color: str) -> Tuple[int, int, int]:
    try:
        return RGB_COLORS[color]
    except KeyError:
        return DEFAULT_COLOR


print(get_color("red"))
