from typing import Dict
from ex0.Card import Card


class CreatureCard(Card):
    def __init__(
        self, name: str, cost: int,
        rarity: str, attack: int, health: int
    ) -> None:
        super().__init__(name, cost, rarity)

        try:
            if (attack < 0 or health < 0):
                raise ValueError("Attack or Health shouldn't be negative!!")
            self.attack: int = attack
            self.health: int = health
        except Exception as e:
            print(e)

    def play(self, game_state: dict) -> dict:
        play_result: Dict = {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "Creature summoned to battlefield"
        }
        return (play_result)

    def attack_target(self, target: str) -> Dict:
        result: Dict = {
            "attacker": self.name,
            "target": target,
            "damage_dealt": self.attack,
            "combat_resolved": True
        }
        return (result)

    def get_card_info(self) -> dict:
        info: Dict = super().get_card_info()
        info.update({
            "type": "Creature",
            "attack": self.attack,
            "health": self.health
        })
        return info
