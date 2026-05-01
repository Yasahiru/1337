from ex0.CreatureCard import CreatureCard
from typing import Dict


def main():
    print("=== DataDeck Card Foundation ===\n")
    print("Testing Abstract Base Class Design:\n")

    fire_dragon: CreatureCard = CreatureCard(
        name="Fire Dragon",
        cost=5,
        rarity="Legendary",
        attack=7,
        health=5
    )
    print(f"CreatureCard Info: {fire_dragon.get_card_info()}\n")

    print("Playing Fire Dragon with 6 mana available:")
    if (fire_dragon.is_playable(6)):
        print("Playable: True")
        print(f"Play result: {fire_dragon.play({})}\n")
    else:
        print("Playable: False\n")

    print("Fire Dragon attacks Goblin Warrior:")
    result: Dict = fire_dragon.attack_target("Goblin Warrior")
    print(f"{result}\n")

    print("Testing insufficient mana (3 available):")
    if (fire_dragon.is_playable(3)):
        print("Playable: True")
        print(f"Play result: {fire_dragon.play({})}\n")
    else:
        print("Playable: False\n")
    print("Abstract pattern successfully demonstrated!")


if __name__ == "__main__":
    main()
