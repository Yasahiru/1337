from mazegen.generator import MazeGenerator


class MazeWriter:
    """Write the maze grid and solution to an output file.

    Attributes:
        maze (MazeGenerator): The generated maze to write.
        output_path (str): Path to the output file.
    """

    def __init__(self, maze: MazeGenerator, output_path: str) -> None:
        """Initialize the MazeWriter.

        Args:
            maze (MazeGenerator): The generated maze instance.
            output_path (str): Path to write the output file.
        """
        self.maze: MazeGenerator = maze
        self.output_path: str = output_path

    def write(self) -> None:
        """Write the maze to the output file.

        The output contains the maze grid encoded in hexadecimal,
        followed by an empty line, then entry coordinates,
        exit coordinates, and the shortest path.
        """

        with open(self.output_path, 'w') as file:
            for row in self.maze.grid.cells:
                grid_row: str = ""
                for cell in row:
                    grid_row += cell.to_hex()
                file.write(grid_row + "\n")

            # Empty line
            file.write('\n')

            entry_x, entry_y = self.maze.entry_point
            exit_x, exit_y = self.maze.exit_point

            file.write(f"{entry_x},{entry_y}\n")
            file.write(f"{exit_x},{exit_y}\n")

            file.write(self.maze.solve() + "\n")
