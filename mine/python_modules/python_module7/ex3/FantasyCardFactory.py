from ex0.CreatureCard import CreatureCard
from ex0.Card import Card
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex3.CardFactory import CardFactory
from typing import Dict  # , List
import random


class FantasyCardFactory(CardFactory):

    def create_creature(
            self, name_or_power: str | int | None = None
    ) -> Card:
        card: Card = None
        if (isinstance(name_or_power, str)):
            card = CreatureCard("Dragon", 5, "LEGENDARY", 7, 5)
        else:
            card = CreatureCard("Goblin Warrior", 2, "LEGENDARY", 4, 3)
        return (card)

    def create_spell(self) -> SpellCard:
        card = SpellCard("Fireball", 3, "RARE", "damage")
        return (card)

    def create_artifact(self, name_or_power) -> ArtifactCard:
        card = ArtifactCard(
            "Mana Crystal", 2,
            "Rare", 12, "Permanent: +1 mana per turn"
        )
        return card

    def create_themed_deck(self, size: int) -> Dict:
        deck = {
            "creatures": self.create_creature(),
            "spells": self.create_spell(),
            "artifacts": self.create_artifact()
        }

        for _ in range(size):
            choice = random.choice(["creature", "spell", "artifact"])

            if choice == "creature":
                deck["creatures"].append(self.create_creature())
            elif choice == "spell":
                deck["spells"].append(self.create_spell())
            else:
                deck["artifacts"].append(self.create_artifact())
        return deck

    def available_types(self):
        return {
            "creatures": ["dragon", "goblin"],
            "spells": ["fireball"],
            "artifacts": ["mana_ring"],
        }

    def get_supported_types(self) -> Dict:
        ...
