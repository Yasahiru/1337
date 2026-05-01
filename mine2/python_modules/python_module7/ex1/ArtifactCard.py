from ex0.Card import Card


class ArtifactCard (Card):
    def __init__(
        self, name: str, cost: int, rarity: str, durability: int, effect: str
    ) -> None:
        super().__init__(name, cost, rarity)
        self.durability: int = durability
        self.effect: str = effect

    def play(self, game_state: dict) -> dict:
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": self.effect
        }

    def activate_ability(self) -> dict:
        ...
