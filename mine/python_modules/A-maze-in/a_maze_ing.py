from mazegen.generators import MazeGenerator as MG
from mazegen.config_parser import Config
from mazegen.display_class import Maze, print_maze
import sys


def main_loop(maze: Maze, conf: Config, solver: MG, msg: bool) -> None:
    show_path = False
    animate: bool = False
    colors = ["\033[42m", "\033[43m", "\033[46m", "\033[47m"]
    color_idx = 0
    path_str = solver.solve(maze)

    while True:
        print_maze(maze, path_str, show_path, colors[color_idx], animate, msg)
        print(
            "\n1: Re-generate | 2: Show/Hide Path | "
            "3: Change Color | 4: Animate | Q: Quit"
        )

        choice = input("Choice? ").lower()
        if choice == "1":
            animate = False
            maze.reset_maze()
            maze_generator = MG(maze, conf.seed)
            maze_generator.generate(conf.algo, conf.perfect)
            path_str = maze_generator.solve(maze)
            maze.save_maze(conf.output_file, path_str)
        elif choice == "2":
            animate = False
            show_path = not show_path
        elif choice == "3":
            animate = False
            color_idx = (color_idx + 1) % len(colors)
        elif choice == "4":
            show_path = True
            animate = True
        elif choice == "q":
            break
        else:
            show_path = False
            animate = False


def main() -> None:
    try:
        if len(sys.argv) != 2:
            print("Usage: python3 a_maze_ing.py config.txt")
            return

        conf = Config()
        conf.load(sys.argv[1])
        maze = Maze(conf.width, conf.height, conf.entry, conf.exit)
        maze_generator = MG(maze, seed=conf.seed)
        msg = maze_generator.generate(conf.algo, conf.perfect)
        path_str = maze_generator.solve(maze)
        maze.save_maze(conf.output_file, path_str)
        main_loop(maze, conf, maze_generator, msg)

    except (ValueError, FileNotFoundError) as e:
        print(f"Error: {e}")
    except (KeyboardInterrupt, EOFError):
        pass


if __name__ == "__main__":
    main()
