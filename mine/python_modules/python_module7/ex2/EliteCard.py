from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical


class EliteCard(Card, Combatable, Magical):

    def __init__(self, name, cost, rarity, attack_power, health, mana):
        super().__init__(name, cost, rarity)

        self.attack_power = attack_power
        self.health = health
        self.defense = 1
        self.mana = mana
        self.spell_power = 2

    # Card:
    def play(self, game_state: dict) -> dict:
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "Elite card deployed"
        }

    # Combatable:
    def attack(self, target: str) -> dict:
        return {
            "attacker": self.name,
            "target": target,
            "damage": self.attack_power,
            "combat_type": "melee"
        }

    def defend(self, incoming_damage: int) -> dict:
        return {
            "defender": self.name,
            "damage_taken": incoming_damage,
            "damage_blocked": incoming_damage,
            "still alive": True if self.health - incoming_damage > 0 else False
        }

    def get_combat_stats(self) -> dict:
        return {
            "attack": self.attack_power,
            "health": self.health,
            "defense": self.defense
        }

    # Magical:
    def cast_spell(self, spell_name: str, targets: list) -> dict:
        mana_cost = 2

        if self.mana < mana_cost:
            return {
                "caster": self.name,
                "spell": spell_name,
                "result": "Not enough mana"
            }

        self.mana -= mana_cost

        return {
            "caster": self.name,
            "spell": spell_name,
            "targets": targets,
            "mana_used": self.mana
        }

    def channel_mana(self, amount: int) -> dict:
        self.mana += amount
        return {
            "channeled": amount,
            "total_mana": self.mana
        }

    def get_magic_stats(self) -> dict:
        return {
            "mana": self.mana,
            "spell_power": self.spell_power
        }
