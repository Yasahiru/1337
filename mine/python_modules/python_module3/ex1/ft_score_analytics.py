import sys


def main() -> None:
    new_av: list[int] = []
    try:
        for av in sys.argv:
            if av != sys.argv[0]:
                int(av)
        print("=== Player Score Analytics ===")
        if (len(sys.argv) <= 1):
            print("No scores provided. Usage: python3"
                  "ft_score_analytics.py <score1> <score2> ...")
        else:
            print("Scores processed ", end="[")
            for av in sys.argv:
                if av != sys.argv[0]:
                    new_av.append(int(av))
                    print(av, end="")
                    if av != sys.argv[len(sys.argv) - 1]:
                        print(",", end=" ")
                    else:
                        print("]")
            print(f"Total players: {len(new_av)}")
            print(f"Total score: {sum(new_av)}")
            print(f"Average score: {sum(new_av) / len(new_av)}")
            print(f"High score: {max(new_av)}")
            print(f"Low score: {min(new_av)}")
            print(f"Score range: {max(new_av) - min(new_av)}\n")
    except ValueError:
        print("Invalid input. Only numbers are allowed !!!")


if __name__ == "__main__":
    main()
