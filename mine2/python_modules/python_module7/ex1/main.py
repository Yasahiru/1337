from ex0.CreatureCard import CreatureCard
from ex1.ArtifactCard import ArtifactCard
from ex1.SpellCard import SpellCard
from ex1.Deck import Deck


def main():
    print()
    print("=== DataDeck Deck Builder ===\n")

    lightning_bolt: SpellCard = SpellCard(
        name="Lightning Bolt",
        cost=3,
        rarity="Common",
        effect_type="Deal 3 damage to target"
    )

    mana_crystal: ArtifactCard = ArtifactCard(
        name="Mana Crystal",
        cost=2,
        rarity="Rare",
        durability=12,
        effect="Permanent: +1 mana per turn"
    )

    fire_dragon: CreatureCard = CreatureCard(
        name="Fire Dragon",
        cost=5,
        rarity="Legendary",
        attack=7,
        health=5
    )

    card_deck = Deck()
    card_deck.add_card(lightning_bolt)
    card_deck.add_card(mana_crystal)
    card_deck.add_card(fire_dragon)
    card_deck.shuffle()

    print("Building deck with different card types...")
    print(f"Deck stats: {card_deck.get_deck_stats()}\n")

    for card in [lightning_bolt, mana_crystal, fire_dragon]:
        if (isinstance(card, CreatureCard)):
            print(f"Drew: {card.name} (Creature)")
        elif (isinstance(card, ArtifactCard)):
            print(f"Drew: {card.name} (Artifact)")
        elif (isinstance(card, SpellCard)):
            print(f"Drew: {card.name} (Spell)")
        print(f"{card.play({})}\n")
    print("Polymorphism in action: Same interface, different card behaviors!")


if __name__ == "__main__":
    main()
