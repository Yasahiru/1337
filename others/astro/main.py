from parser import parse_inputs
from AsteroidAnalyzer import AsteroidAnalyzer
from result_ui import ResultUI
import tkinter as tk


def main():
    data = parse_inputs()

    asteroid = AsteroidAnalyzer(data)
    result = asteroid.analyze_asteroid()

    root = tk.Tk()
    root.title("Astro Smart System")
    root.geometry("1000x1000")

    result_ui = ResultUI(root)
    result_ui.show_result(result)

    root.mainloop()


if __name__ == "__main__":
    main()