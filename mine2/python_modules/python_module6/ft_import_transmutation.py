import alchemy.elements
from alchemy.elements import create_water, create_fire
from alchemy.potions import strength_potion
from alchemy.potions import healing_potion as heal

[create_water, create_fire, heal, alchemy.elements]


def main():
    try:
        print("=== Import Transmutation Mastery ===\n")
        print("Method 1 - Full module import:")
        print(
                "alchemy.elements.create_fire(): "
                f"{alchemy.elements.create_fire()}\n"
            )

        print("Method 2 - Specific function import:")
        print(f"create_water(): {create_water()}\n")

        print("Method 3 - Aliased import:")
        print(f"heal(): {heal(create_fire(), create_water())}\n")

        print("Method 4 - Multiple imports:")
        print(f"create_earth(): {alchemy.elements.create_earth()}")
        print(f"create_fire(): {create_fire()}")
        print(f"strength_potion(): {
                strength_potion(alchemy.elements.create_earth(), create_fire())
            } \n"
        )

        print("All import transmutation methods mastered!")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
