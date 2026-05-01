import sys
import math


def Euclidean_formula(
            original_position: tuple, second_position: tuple
        ) -> float:
    return math.sqrt((second_position[0] - original_position[0]) ** 2 +
                     (second_position[1] - original_position[1]) ** 2 +
                     (second_position[2] - original_position[2]) ** 2)


def ft_coordinate_system() -> None:
    try:
        if (len(sys.argv) == 1):
            coordinates = (10, 20, 5)
            default = (0, 0, 0)
            print(f"Position Created: {coordinates}")
            print(
                    f"Distance between {default} and {coordinates}: "
                    f"{round(Euclidean_formula(default, coordinates), 2)}\n"
                )
        else:
            coordinates = (10, 20, 5)
            default = (0, 0, 0)
            print(f"Position Created: {coordinates}")
            print(
                    f"Distance between {default} and {coordinates}: "
                    f"{round(Euclidean_formula(default, coordinates), 2)}\n"
                )
            print(f"Parsing coordinates: \"{sys.argv[1]}\"")
            for av in sys.argv:
                if av != sys.argv[0]:
                    arguments = av.split(",")
                    for arg in arguments:
                        int(arg)
            if (len(sys.argv) == 2):
                arguments: list[str] = sys.argv[1].split(",")

                if (len(arguments) == 3):
                    default = (0, 0, 0)
                    parsed_coordinates: list[int] = []

                    for arg in arguments:
                        parsed_coordinates.append(int(arg))
                    coordinates = tuple(parsed_coordinates)
                    print(f"Parsed position: {coordinates}")
                    print(
                        f"Distance between {default} and {coordinates}: "
                        f"{round(Euclidean_formula(default, coordinates), 2)}"
                        "\n"
                    )
        print("Unpacking demonstration:")
        print(f"Player at x={coordinates[0]}, y={coordinates[1]},"
              f" z={coordinates[2]}")
        print(f"Coordinates: X={coordinates[0]}, Y={coordinates[1]},"
              f" Z={coordinates[2]}")
    except ValueError as e:
        print(e)
        print(f"Error details - Type: ValueError, Args (\"{e}\",)")


def main() -> None:
    print("=== Game Coordinate System ===\n")
    ft_coordinate_system()


if __name__ == "__main__":
    main()
