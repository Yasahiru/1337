from collections.abc import Callable


def fireball(target: str, power: int) -> str:
    return f"Fireball hits {target} for {power} damage"


def heal(target: str, power: int) -> str:
    return f"Heal restores {target} for {power} HP"


def lightning(target: str, power: int) -> str:
    return f"Lightning strikes {target} for {power} damage"


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combined(target: str, power: int) -> tuple:
        result1 = spell1(target, power)
        result2 = spell2(target, power)
        return (result1, result2)
    return combined


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def amplified(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)
    return amplified


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def conditional(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        return "Spell fizzled"
    return conditional


def spell_sequence(spells: list[Callable]) -> Callable:
    def sequence(target: str, power: int) -> list:
        results = []
        for spell in spells:
            results.append(spell(target, power))
        return results
    return sequence


def strong_enough(target: str, power: int) -> bool:
    return power >= 5


def main() -> None:
    print("=== Testing spell_combiner ===")
    combined = spell_combiner(fireball, heal)
    print(combined("Dragon", 10))
    print(spell_combiner.gi_frame.f_locals)

    print("\n=== Testing power_amplifier ===")
    mega_fireball = power_amplifier(fireball, 3)
    print("Original:", fireball("Goblin", 5))
    print("Amplified:", mega_fireball("Goblin", 5))

    print("\n=== Testing conditional_caster ===")
    safe_fireball = conditional_caster(strong_enough, fireball)
    print(safe_fireball("Orc", 3))
    print(safe_fireball("Orc", 6))

    print("\n=== Testing spell_sequence ===")
    sequence = spell_sequence([fireball, heal, lightning])
    results = sequence("Knight", 4)
    for result in results:
        print(result)


if __name__ == "__main__":
    main()
