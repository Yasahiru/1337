

def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(
        artifacts,
        key=lambda a: a["power"],
        reverse=True
    )


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return (
        list(
            filter(lambda m: m["power"] >= min_power, mages)
        )
    )


def spell_transformer(spells: list[str]) -> list[str]:
    return (
        list(
            map(lambda s: f"* {s} *", spells)
        )
    )


def mage_stats(mages: list[dict]) -> dict:
    return {
        "max": max(mages, key=lambda a: a["power"])["power"],
        "min": min(mages, key=lambda a: a["power"])["power"],
        "avg": sum(
            map(
                lambda s: s["power"], mages
            )
        ) / len(mages)
    }


def main() -> None:
    artifacts = [
        {'name': 'Shadow Blade', 'power': 96, 'type': 'armor'},
        {'name': 'Shadow Blade', 'power': 91, 'type': 'weapon'},
        {'name': 'Water Chalice', 'power': 120, 'type': 'weapon'},
        {'name': 'Shadow Blade', 'power': 101, 'type': 'focus'}
    ]

    mages = [
        {'name': 'River', 'power': 97, 'element': 'water'},
        {'name': 'Ash', 'power': 62, 'element': 'earth'},
        {'name': 'Jordan', 'power': 88, 'element': 'light'},
        {'name': 'Luna', 'power': 56, 'element': 'fire'},
        {'name': 'Sage', 'power': 72, 'element': 'fire'}
    ]

    spells = ['earthquake', 'freeze', 'shield', 'heal']

    print("Testing artifact sorter...")
    sorted_artifacts = artifact_sorter(artifacts)
    for a in sorted_artifacts:
        print(f"{a['name']} ({a['power']} power)")

    print("\nTesting power filter...")
    print(power_filter(mages, 70))

    print("\nTesting spell transformer...")
    print(spell_transformer(spells))

    print("\nTesting mage stats...")
    print(mage_stats(mages))


if __name__ == "__main__":
    main()
