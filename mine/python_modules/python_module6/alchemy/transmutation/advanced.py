from .basic import lead_to_gold
from ..potions import healing_potion
import alchemy


def philosophers_stone() -> str:
    return (
        f"Philosopher’s stone created using {lead_to_gold()}"
        f" and {
            healing_potion(
              alchemy.create_fire(),
              alchemy.create_water()
            )
        }"
    )


def elixir_of_life() -> str:
    return (
        "Elixir of life: eternal youth achieved!"
    )
