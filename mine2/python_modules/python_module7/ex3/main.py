from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.AggressiveStrategy import AggressiveStrategy
from ex3.GameEngine import GameEngine


def main():

    try:
        print("=== DataDeck Game Engine ===\n")

        factory = FantasyCardFactory()
        strategy = AggressiveStrategy()

        print("Configuring Fantasy Card Game...")
        print("Factory:", factory.__class__.__name__)
        print("Strategy:", strategy.__class__.__name__)
        print("Available types:", factory.available_types())

        engine = GameEngine()
        engine.configure_engine(factory, strategy, 1)

        print("\nSimulating aggressive turn...")
        print("Hand:", end=" ")
        for card in engine.hand:
            print(card.name, end=" ")
            print(f" ({card.cost})", end=", ")

        actions = engine.simulate_turn()

        print("\n\nTurn execution:")
        print("Strategy:", strategy.__class__.__name__)
        print("Actions:", actions)

        report = engine.get_engine_status()

        print("\nGame Report:")
        print(report)

        print("\nAbstract Factory + Strategy Pattern:"
              " Maximum flexibility achieved!")

    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
