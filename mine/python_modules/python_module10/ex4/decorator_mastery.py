from collections.abc import Callable
from functools import wraps
import time


def spell_timer(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Casting {func.__name__}...")
        start = time.time()

        result = func(*args, **kwargs)

        end = time.time()
        print(f"Spell completed in {end - start:.2f} seconds")

        return result
    return wrapper


def power_validator(min_power: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):

            if len(args) >= 3:
                power = args[2]
            else:
                power = args[0]

            if power < min_power:
                return "Insufficient power for this spell"

            return func(*args, **kwargs)

        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    print(
                        "Spell failed, retrying... "
                        f"(attempt {attempt}/{max_attempts})"
                    )

            return f"Spell casting failed after {max_attempts} attempts"

        return wrapper
    return decorator


class MageGuild:

    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if len(name) < 3:
            return False

        for c in name:
            if not (c.isalpha() or c.isspace()):
                return False

        return True

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


if __name__ == "__main__":

    print("Testing spell timer...")

    @spell_timer
    def fireball():
        time.sleep(0.1)
        return "Fireball cast!"

    print("Result:", fireball())

    print("\nTesting retrying spell...")

    @retry_spell(3)
    def unstable_spell():
        raise Exception("fail")

    print(unstable_spell())

    @retry_spell(3)
    def success_spell():
        return "Waaaaaaagh spelled !"

    print(success_spell())

    print("\nTesting MageGuild...")

    print(MageGuild.validate_mage_name("Merlin"))
    print(MageGuild.validate_mage_name("12"))

    mage = MageGuild()
    print(mage.cast_spell("Lightning", 15))
    print(mage.cast_spell("Lightning", 5))
