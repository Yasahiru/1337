from maze.fake_generator import generate_fake_maze

def main():
    maze = generate_fake_maze(20, 10)

    print("Maze size:", maze.width, "x", maze.height)
    print("Entry:", maze.entry)
    print("Exit:", maze.exit)

if __name__ == "__main__":
    main()