from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.ArtifactCard import ArtifactCard
from ex1.SpellCard import SpellCard

from typing import List
import random


class Deck():
    def __init__(self):
        self.cards: List[Card] = []

    def add_card(self, card: Card) -> None:
        self.cards.append(card)

    def remove_card(self, card_name: str) -> bool:
        for card in self.cards:
            if card.name == card_name:
                self.cards.remove(card)
                return True
        return False

    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def draw_card(self) -> Card:
        try:
            return self.cards.pop()
        except Exception as e:
            print(e)
            return None

    def get_deck_stats(self) -> dict:
        try:
            creatures: int = 0
            spells: int = 0
            artifacts: int = 0
            cost: int = 0
            avg_cost: float = 0

            for card in self.cards:
                if (isinstance(card, CreatureCard)):
                    creatures += 1
                    cost += card.cost
                elif (isinstance(card, ArtifactCard)):
                    artifacts += 1
                    cost += card.cost
                elif (isinstance(card, SpellCard)):
                    spells += 1
                    cost += card.cost

            total_cards = len(self.cards)
            avg_cost = cost / total_cards if total_cards > 0 else 0

            return {
                "total_cards": total_cards,
                "creatures": creatures,
                "spells": spells,
                "artifacts": artifacts,
                "avg_cost": round(avg_cost, 1)
            }
        except Exception as e:
            print(e)
