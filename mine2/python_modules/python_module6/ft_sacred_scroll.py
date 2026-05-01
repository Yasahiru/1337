
import alchemy


def main():
    try:
        print("=== Sacred Scroll Mastery ===\n")
        print("Testing direct module access:")

        print(
                "alchemy.elements.create_fire(): "
                f"{alchemy.elements.create_fire():}"
            )
        print(
                "alchemy.elements.create_water(): "
                f"{alchemy.elements.create_water():}"
            )
        print(
                "alchemy.elements.create_earth(): "
                f"{alchemy.elements.create_earth():}"
            )
        print(
                "alchemy.elements.create_air(): "
                f"{alchemy.elements.create_air():}\n"
            )

        print("Testing package-level access (controlled by __init__.py):")

        print(
            "alchemy.create_fire():"
            f"{alchemy.create_fire()}"

        )
        print(
            "alchemy.create_water():"
            f"{alchemy.create_water()}"
        )

        try:
            print(
                "alchemy.create_earth():"
                f"{alchemy.create_earth()}"
            )
        except Exception:
            print("alchemy.create_earth(): AttributeError - not exposed")

        try:
            print(
                "alchemy.create_air():"
                f"{alchemy.create_air()}"
            )
        except Exception:
            print("alchemy.create_air(): AttributeError - not exposed")

        print()
        print("Package metadata:")
        print(f"Version: {alchemy.__version__}")
        print(f"Author: {alchemy.__author__}")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
