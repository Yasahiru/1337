from ex2.EliteCard import EliteCard


def main():
    print("=== DataDeck Ability System ===\n")
    print("EliteCard capabilities:")
    print("- Card: ['play', 'get_card_info', 'is_playable']")
    print("- Combatable: ['attack', 'defend', 'get_combat_stats']")
    print("- Magical: ['cast_spell', 'channel_mana', 'get_magic_stats']\n")
    print("Playing Arcane Warrior (Elite Card):\n")

    arcane_warrior = EliteCard(
        name="Arcane Warrior",
        cost=5,
        rarity="Legendary",
        attack_power=5,
        mana=12,
        health=10
    )

    print("Combat phase")
    print(f"Attack result: {arcane_warrior.attack("Enemy")}")
    print(f"Defence result: {arcane_warrior.defend(2)}\n")

    print("Magic phase")
    print(f"Spell cast: {arcane_warrior.cast_spell(
        "Fireball", ['Enemy1', 'Enemy2']
    )}")
    print(f"Mana channel: {arcane_warrior.channel_mana(3)}\n")

    print("Multiple interface implementation successful!")


if __name__ == "__main__":
    main()
