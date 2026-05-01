from functools import reduce, partial, lru_cache, singledispatch
from collections.abc import Callable
from typing import Dict, Any
import operator
import sys


def spell_reducer(spells: list[int], operation: str) -> int:
    ops = {
        "add": operator.add,
        "multiply": operator.mul,
        "max": max,
        "min": min,
    }
    try:
        result = reduce(ops.get(operation), spells)
    except Exception:
        print("Unknown operation")
        sys.exit()
    return result


def partial_enchanter(base_enchantment: Callable) -> Dict[str, Callable]:
    fire_spell = partial(base_enchantment, 50, "fire")
    ice_spell = partial(base_enchantment, 50, "ice")
    earth_spell = partial(base_enchantment, 50, "earth")
    return {
        "fire": fire_spell,
        "ice": ice_spell,
        "earth": earth_spell
    }


@lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n <= 1:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher():
    @singledispatch
    def dispatch(x: Any) -> str:
        return "Unknown spell type"

    @dispatch.register(int)
    def _(x: int) -> str:
        return f"Damage spell: {x} damage"

    @dispatch.register(str)
    def _(x: str) -> str:
        return f"Enchantment: {x}"

    @dispatch.register(list)
    def _(x: list) -> str:
        return f"Multi-cast: {len(x)} spells"

    return dispatch


def main() -> None:
    spell_powers = [19, 26, 17, 49, 32, 18]
    operations = ['add', 'multiply', 'max', 'min']
    fibonacci_tests = [16, 10, 9]

    print("\nTesting spell reducer...")
    for op in operations:
        res = spell_reducer(
            spell_powers,
            op
        )
        print(res)

    print("\nTesting memoized fibonacci...")
    for fibo in fibonacci_tests:
        print(
            f"Fib({fibo}): "
            f"{memoized_fibonacci(fibo)}"
        )

    print("\nTesting spell dispatcher...")
    spell = spell_dispatcher()
    print(spell(42))
    print(spell("fireball"))
    print(spell([1, 2, 3]))
    print(spell(None))


def base_enchantment(power: int, element: str, target: str) -> str:
    return f"{element} hits {target} with power {power}"


if __name__ == "__main__":
    main()
