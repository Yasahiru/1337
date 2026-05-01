from collections.abc import Callable
from typing import Dict, Any


def mage_counter() -> Callable:
    times: int = 0

    def count() -> int:
        nonlocal times
        times += 1
        return times
    return count


def spell_accumulator(initial_power: int) -> Callable:
    _initial_power = initial_power

    def accumulator(power: int) -> int:
        nonlocal _initial_power
        _initial_power += power
        return (_initial_power)
    return accumulator


def enchantment_factory(enchantment_type: str) -> Callable:
    def enchant(enchantment_util: str) -> str:
        return f"{enchantment_type} {enchantment_util}"
    return enchant


def memory_vault() -> Dict[str, Callable]:
    _dict = dict({})

    def store(key: str, value: Any) -> None:
        _dict[key] = value

    def recall(key: str) -> Any:
        return _dict.get(key, "Memory not found")

    return {
        "store": store,
        "recall": recall
    }


def main() -> None:

    print("Testing mage_counter...")
    counter_a = mage_counter()
    counter_b = mage_counter()
    print("counter_a call 1:", counter_a())
    print("counter_a call 2:", counter_a())
    print("counter_b call 1:", counter_b())

    print("\nTesting spell_accumulator...")
    acc = spell_accumulator(100)
    print("Base 100, add 20:", acc(20))
    print("Base 100, add 30:", acc(30))

    print("\nTesting enchantment_factory...")
    flame = enchantment_factory("Flaming")
    frost = enchantment_factory("Frozen")
    print(flame("Sword"))
    print(frost("Shield"))

    print("\nTesting memory_vault...")
    vault = memory_vault()
    print("Store 'secret' = 42")
    vault["store"]("secret", 42)
    print("Recall 'secret':", vault["recall"]("secret"))
    print("Recall 'unknown':", vault["recall"]("unknown"))


if __name__ == "__main__":
    main()
