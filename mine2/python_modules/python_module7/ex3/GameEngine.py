# from ex0.Card import Card
from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy
# from typing import List


class GameEngine:
    def configure_engine(
        self, factory: CardFactory, strategy: GameStrategy,
        turn_count: int
    ) -> None:
        self.strategy = strategy
        self.factory = factory
        self.hand = [
            factory.create_creature(),
            factory.create_creature(),
            factory.create_spell(),
        ]
        self.battlefield = "arena"
        self.turn_count = turn_count

    def simulate_turn(self) -> dict:
        result = self.strategy.execute_turn(self.hand, self.battlefield)
        self.turn_count += 1
        return result

    def get_engine_status(self) -> dict:
        return {
            "turns_simulated": self.turn_count,
            "strategy_used": self.strategy.__class__.__name__,
            "total_damage": "damage_dealt",
            "cards_created": len(self.hand),
        }
