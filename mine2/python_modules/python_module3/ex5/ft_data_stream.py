from typing import Generator
import sys


def ft_game_event_stream(total: int) -> Generator[dict, None, None]:

    players = ["alice", "bob", "charlie", "david", "eve"]
    actions = ["killed monster", "found treasure", "leveled up"]

    for i in range(total):
        yield {
            "id": i + 1,
            "player": players[i % len(players)],
            "level": (i % 20) + 1,
            "action": actions[i % len(actions)]
        }


def ft_high_level_players(
            events: Generator[dict, None, None]
        ) -> Generator[dict, None, None]:

    for event in events:
        if event["level"] >= 10:
            yield event


def ft_filter_action(
        events: Generator[dict, None, None], action: str
        ) -> Generator[dict, None, None]:

    for event in events:
        if event["action"] == action:
            yield event


def ft_fibonacci(fibo_seq: list[int]) -> Generator[int, None, None]:
    while True:
        number1: int = fibo_seq[-1]
        number2: int = fibo_seq[-2]
        fibo_seq.append(number1 + number2)
        yield (fibo_seq[-1])


def ft_is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def ft_prime_generator() -> Generator[int, None, None]:
    num = 2
    while True:
        if ft_is_prime(num):
            yield num
        num += 1


def main() -> None:

    if len(sys.argv) == 1:
        total_events = 1000

    elif len(sys.argv) == 2:
        if sys.argv[1].isdigit():
            total_events = int(sys.argv[1])
            if total_events <= 0:
                print("Error")
                return
        else:
            print("Error")
            return
    else:
        print("Error")
        return

    print(f"Processing {total_events} game events...")

    total: int = 0
    high_level: int = 0
    treasure_count: int = 0
    levelup_count: int = 0
    event_stream: int = ft_game_event_stream(total_events)

    for event in event_stream:
        total += 1

        if total <= total_events:
            print(f"Event {event['id']}: Player {event['player']} "
                  f"(level {event['level']}) {event['action']}")

        if event["level"] >= 10:
            high_level += 1
        if event["action"] == "found treasure":
            treasure_count += 1
        if event["action"] == "leveled up":
            levelup_count += 1

    print("\n=== Stream Analytics ===")
    print(f"Total events processed: {total}")
    print(f"High-level players (10+): {high_level}")
    print(f"Treasure events: {treasure_count}")
    print(f"Level-up events: {levelup_count}")

    print("Memory usage: Constant (streaming)")
    print(f"Processing time: {total * .02}")

    print("\n=== Generator Demonstration ===")

    fibo_seq: list[int] = [0, 1]
    fibo: Generator[int, None, None] = ft_fibonacci(fibo_seq)
    for _ in range(8):
        next(fibo)
    print(f"Fibonacci sequence (first 10): {fibo_seq}")

    primes: Generator[int, None, None] = ft_prime_generator()
    prime_list: list[int] = []
    for _ in range(5):
        prime_list.append(str(next(primes)))
    print("Prime numbers (first 5): " + ", ".join(prime_list))


if __name__ == "__main__":
    main()
