from ex3.GameStrategy import GameStrategy
# from typing import Dict
# import random


class AggressiveStrategy(GameStrategy):
    def execute_turn(self, hand: list, battlefield: list) -> dict:
        cards_played = []
        mana_used = 0
        damage = 0

        for card in hand:
            if card.name in ["Goblin Warrior", "Lightning Bolt"]:
                cards_played.append(card.name)
                mana_used += card.cost
                damage += card.cost

        return {
            "cards_played": cards_played,
            "mana_used": mana_used,
            "targets_attacked": ["Enemy Player"],
            "damage_dealt": damage,
        }

    def get_strategy_name(self) -> str:
        return ("AggressiveStrategy")

    def prioritize_targets(self, available_targets: list) -> list:
        return sorted(
            available_targets,
            key=lambda t: getattr(t, "power", 0),
            reverse=True
        )
