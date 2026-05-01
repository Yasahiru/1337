import alchemy.grimoire


def main():
    try:
        print("\n=== Circular Curse Breaking ===\n")

        print("Testing ingredient validation:")
        print(
            "validate_ingredients(\"fire air\") "
            f"{alchemy.grimoire.validate_ingredients("fire air")}"
        )
        print(
            "validate_ingredients(\"dragon scales\"): "
            f"{alchemy.grimoire.validate_ingredients("dragon scales")}"
        )

        print()

        print("Testing spell recording with validation:")
        print(
            "record_spell(\"Fireball\", \"fire air\"): "
            f"{alchemy.grimoire.record_spell("Fireball", "fire air")}"
        )
        print(
            "record_spell(\"Dark Magic\", \"shadow\"): "
            f"{alchemy.grimoire.record_spell("Dark Magic", "shadow")}"
        )

        print()

        print("Testing late import technique:")
        from alchemy.grimoire import record_spell
        print(
            "record_spell(\"Lightning\", \"air\"): "
            f"{record_spell("Lightning", "air"):}"
        )

        print()
        print("Circular dependency curse avoided using late imports!")
        print("All spells processed safely!")

    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
