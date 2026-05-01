from ex0.Card import Card
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable


class TournamentCard(Card, Combatable, Rankable):

    def __init__(self, name, cost, rarity):
        super().__init__(name, cost, rarity)
        self.rating = 1000
        self.wins = 0
        self.losses = 0
        self.card_id = f"{name}_001"

    def play(self, game_state: dict) -> dict:
        return {"action": f"{self.name} played"}

    def attack(self, target) -> bool:
        return self.cost >= target.cost

    def defend(self, attacker) -> bool:
        return self.cost >= attacker.cost

    def get_combat_stats(self) -> dict:
        return {
            "cost": self.cost
        }

    def calculate_rating(self) -> int:
        return self.rating

    def update_wins(self, wins: int) -> None:
        self.wins += wins

    def update_losses(self, losses: int) -> None:
        self.losses += losses

    def get_rank_info(self) -> dict:
        return {
            "rating": self.rating,
            "wins": self.wins,
            "losses": self.losses
        }

    def record(self) -> str:
        return f"{self.wins}W-{self.losses}L"
