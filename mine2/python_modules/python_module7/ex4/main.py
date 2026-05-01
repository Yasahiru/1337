from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlatform


def main():
    print("=== DataDeck Tournament Platform ===\n")

    platform = TournamentPlatform()

    print("Registering Tournament Cards...\n")

    card1 = TournamentCard("Fire Dragon", 12, "RARE")
    card2 = TournamentCard("Ice Wizard", 10, "COMMON")

    id1 = platform.register_card(card1)
    id2 = platform.register_card(card2)

    for card in platform.cards.values():
        print(f"{card.name} (ID: {card.card_id}):")
        print("- Interfaces: [Card, Combatable, Rankable]")
        print(f"- Rating: {card.rating}")
        print(f"- Record: {card.record()}\n")

    result = platform.create_match("dragon_001", "wizard_001")
    print("Creating tournament match...")

    result = platform.create_match(id1, id2)
    print(f"Match result: {result}\n")

    print("Tournament Leaderboard:")

    leaderboard = platform.get_leaderboard()
    for i, card in enumerate(leaderboard, 1):
        print(f"{i}. {card.name} - Rating: {card.rating} ({card.record()})")

    print("\nPlatform Report:")
    print(platform.generate_tournament_report())

    print("\n=== Tournament Platform Successfully Deployed! ===")
    print("All abstract patterns working together harmoniously!")


if __name__ == "__main__":
    main()
