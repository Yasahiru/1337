from srcs.generators import MazeGenerator
from srcs.config_parser import Config
from srcs.solve_maze import MazeSolver
from srcs.display_class import Maze, print_maze
import sys


def main_loop(maze_obj: Maze, conf: Config, solver: MazeSolver) -> None:
    show_path = False
    animate: bool = False
    colors = ["\033[42m", "\033[43m", "\033[46m", "\033[47m"]
    color_idx = 0
    path_str = solver.solve(maze_obj)

    while True:
        print_maze(maze_obj, path_str, show_path, colors[color_idx], animate)
        print(
            "\n1: Re-generate | 2: Show/Hide Path | "
            "3: Change Color | 4: Animate | Q: Quit"
        )

        choice = input("Choice? ").lower()
        if choice == "1":
            animate = False
            maze_obj.reset_maze()
            maze_generator = MazeGenerator(maze_obj, conf.seed)
            maze_generator.generate(conf.algo, conf.perfect)
            path_str = solver.solve(maze_obj)
            maze_generator.save_maze(conf.output_file, path_str)
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


def main():
    try:
        conf = Config()
        conf.load(sys.argv[1])
        maze = Maze(conf.width, conf.height, conf.entry, conf.exit)
        maze_generator = MazeGenerator(maze, seed=conf.seed)
        maze_generator.generate(algorithm=conf.algo, perfect=conf.perfect)
        solver = MazeSolver()
        main_loop(maze, conf, solver)

    except (ValueError, FileNotFoundError) as e:
        print(f"Error: {e}")
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
