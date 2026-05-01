import curses
import curses.panel
import random
from typing import Dict
import time
from collections import deque
from curses.textpad import Textbox, rectangle


from typing import Dict, Any
from validate_config import validate
from Errors import InvalidEntryError, InvalidFileError, InvalidArgumentError
from mazegen import MazeGenerator, MazeWriter, cell

import sys
import os



type CWindow = curses.window
type Maze = MazeGenerator



def center_text(win : CWindow, texte : str, y : int):
    _, width = win.getmaxyx()
    x = (width - len(texte)) // 2
    win.addstr(y, x - 1, texte)

def center_text_win(win, texte):
    height, width = win.getmaxyx()
    lignes = texte.split("\n")
    start_y = (height - len(lignes)) // 2
    for i, ligne in enumerate(lignes):
        x = (width - len(ligne)) // 2
        win.addstr(start_y + i, x, ligne)

def create_win_with_panel(h, w, y, x, title, color_pair = 0):
    win = curses.newwin(h, w, y, x)
    win.bkgd(' ', curses.color_pair(color_pair))
    win.box()
    win.addstr(0, 1, title)
    panel = curses.panel.new_panel(win)
    panel.hide()
    return win, panel



class Display:
    stdscr: CWindow
    menu_win: CWindow
    maze: Maze
    error_mod : bool
    maze_state : bool


    def __init__(self, maze: Maze, stdscr: CWindow) -> None:
        # initial state of the program (at the start)
        self.INITIAL_STATE : bool = True
        self.theme = "dark"

        self.maze = maze
        self.path : str = self.maze.solve()

        curses.start_color()
        curses.use_default_colors()

        curses.init_color(BLACK, 50, 55, 75)
        curses.init_color(RED, 600, 300, 350)
        curses.init_color(GREEN, 400, 550, 480)
        curses.init_color(YELLOW, 650, 550, 350)
        curses.init_color(BLUE, 400, 500, 700)
        curses.init_color(MAGENTA, 600, 450, 650)
        curses.init_color(CYAN, 400, 600, 650)
        curses.init_color(WHITE, 600, 650, 750)


        self.maze_is_animating : bool = False
        self.path_is_animating : bool = False
        self.togle_animation : bool = True
        self.path_shown : bool = False


        self.maze_animation_step : int = 0
        self.maze_animation_step_number : int = 1
        self.last_time_maze_animation : float = time.time()

        self.maze_animation_types : dict = {
            "line by line" : self.line_by_line_maze_animation,
            "cell by cell" : self.cell_by_cell_maze_animation,
            "random" : self.random_maze_animation,
            "prim" : self.prim_maze_animation,
            "spread" : self.spread_maze_animation,
            "oil effect" : self.oil_effect_maze_animation,
        }

        self.path_animation_step : int = 0
        self.last_time_path_animation : float = time.time()


        self.stdscr = stdscr
        curses.curs_set(False)
        self.stdscr.nodelay(True)
        self.stdscr.box()
        self.scr_height, self.scr_width = stdscr.getmaxyx()


        # menu options
        self.menu_state = "main"

        self.selectors_data = {
            "animation" : [(key, func) for key, func in self.maze_animation_types.items()],
            "walls color" : [("white", 1), ("cyan", 2), ("blue", 3), ("green", 4), ("red", 5), ("yellow", 6), ("magenta", 7)],
            "path color" : [("cyan", 2), ("blue", 3)],
            "theme" : [("dark", "dark"), ("light", "light")],
            "perfect " : [("on", True), ("off", False)],
        }
        self.selectors_indexes = {
            "animation" : 0,
            "walls color" : 0,
            "path color" : 0, 
            "theme" : 0,
            "perfect " : 0,
        }

        self.current_animation : str = self.selectors_data["animation"][self.selectors_indexes["animation"]][0]

        self.main_menu = {
            ("generate", "button") : self.generate,
            ("show path", "button") : self.show_path,
            ("maze config", "button") : self.open_config_menu,
            ("custom option", "button") : self.open_animation_menu,
            ("exit", "button") : self.exit_programme,
        }

        self.config = {
            "width" : self.maze.width,
            "height" : self.maze.height,
            "entry" : self.maze.entry_point,
            "exit" : self.maze.exit_point,
            "seed" : self.maze.seed,
            "perfect" : self.maze.perfect,
        }
        self.config_menu = {
            (f"width : {self.config["width"]}", "button") : self.width_config_button,
            (f"height : {self.config["height"]}", "button") : self.height_config_button,
            (f"entry : {self.config["entry"]}", "button") : self.entry_config_button,
            (f"exit : {self.config["exit"]}", "button") : self.exit_config_button,
            (f"seed : {self.config["seed"] if self.config["seed"] else "random"}", "button") : self.seed_config_button,
            (f"perfect ", "selector") : None,
            ("back", "button") : self.back_to_main_menu,
        }

        self.customization_menu = {
            ("animation", "selector") : None,
            ("walls color", "selector") : None,
            ("path color", "selector") : None,
            ("theme", "selector") : None,
            ("back", "button") : self.back_to_main_menu, 
        }
        self.menu_options = self.main_menu
        self.selected_vertical_index = 0

        self.input_mod = False
        self.input_done = False
        self.input_come_from : str


        try:
            self.create_maze()
            self.create_menu()
            self.create_help()
            self.create_input_popup("")
            self.create_error_popup()
            self.error_mod = False
        except curses.error:
            self.create_error_popup()
            self.error_mod = True


    def width_config_button(self) -> None:
        self.create_input_popup("width:")
        self.show_input_popup()
        self.input_mod = True
        self.input_come_from = "width"

    def height_config_button(self) -> None:
        self.create_input_popup("height:")
        self.show_input_popup()
        self.input_mod = True
        self.input_come_from = "height"

    def seed_config_button(self) -> None:
        self.create_input_popup("seed:")
        self.show_input_popup()
        self.input_mod = True
        self.input_come_from = "seed"

    def entry_config_button(self) -> None:
        self.create_input_popup("entry:")
        self.show_input_popup()
        self.input_mod = True
        self.input_come_from = "entry"

    def exit_config_button(self) -> None:
        self.create_input_popup("exit:")
        self.show_input_popup()
        self.input_mod = True
        self.input_come_from = "exit"




    def create_input_popup(self, label : str) -> None:
        self.input_height = 3
        self.input_width  = 20
        self.input_y = self.menu_y + self.menu_height - 2
        self.input_x = self.menu_x + (self.menu_width // 4)
        self.input_win, self.input_panel = create_win_with_panel(
            self.input_height,
            self.input_width,
            self.input_y,
            self.input_x,
            label,
            1
        )
        self.sub_input_win = self.input_win.derwin(1, 18, 1, 1)
        self.input_box = Textbox(self.sub_input_win)

    def show_input_popup(self) -> None:
        if self.input_panel.hidden():
            self.input_panel.show()
            self.input_panel.top()


    def create_error_popup(self) -> None:
        try:
            self.error_popup_win, self.popup_panel = create_win_with_panel(
                self.scr_height,
                self.scr_width,
                0,
                0,
                "pop up!",
                5

            )
            center_text_win(self.error_popup_win, f"resize windows!{self.scr_height}x{self.scr_width}")
        except curses.error:
            pass


    def show_error_popup(self) -> None:
        if self.popup_panel.hidden():
            self.popup_panel.show()
            self.popup_panel.top()


    def create_help(self) -> None:
        self.help_height = self.scr_height // 4 - 1
        self.help_width  = self.scr_width // 2 - 1
        self.help_y = (self.scr_height - self.help_height) // 2
        self.help_x = (self.scr_width - self.help_width) // 2
        self.help_win, self.help_panel = create_win_with_panel(
            self.help_height,
            self.help_width,
            self.help_y,
            self.help_x,
            "help:",
            1
        )

        help_option = """\
space: toggle maze animation
k/⭡-j/⭣: navigate up/down
"""
        center_text_win(self.help_win, help_option)


    def show_help(self) -> None:
        if self.help_panel.hidden():
            self.help_panel.show()
            self.help_panel.top()
        else:
            self.help_panel.hide()



    def create_menu(self) -> None:
        self.menu_height = self.scr_height // 4 - 1
        # self.menu_width  = self.scr_width // 2 + 12
        self.menu_width  = 40
        self.menu_y = self.scr_height - self.scr_height // 4
        self.menu_x = (self.scr_width - self.menu_width) // 2
        self.menu_win, self.menu_panel = create_win_with_panel(
            self.menu_height,
            self.menu_width,
            self.menu_y,
            self.menu_x,
            "",
            1
        )
        self.menu_win.keypad(True)
        self.menu_win.nodelay(True)

    def show_menu(self) -> None:
        if self.menu_panel.hidden():
            self.menu_panel.show()
            self.menu_panel.top()

    def create_maze(self) -> None:
        self.maze_height = (self.scr_height  * 3) // 4 - 1 
        self.maze_width  = self.scr_width - 2
        self.maze_y = 1
        self.maze_x = 1
        self.maze_win, self.maze_panel = create_win_with_panel(
            self.maze_height,
            self.maze_width,
            self.maze_y,
            self.maze_x,
            "disp",
            1
        )
        self.maze_win.nodelay(True)

    def show_maze(self) -> None:
        if self.maze_panel.hidden():
            self.maze_panel.show()
            self.maze_panel.top()


    def draw_menu(self) -> None:
        menu_win = self.menu_win
        menu_win.erase()
        menu_win.box()


        menu_win.addstr(0, 2, f"{self.menu_state}:", curses.A_DIM | curses.A_REVERSE)
        menu_win.addstr(self.menu_height - 1, 2, f"(?=help)", curses.A_DIM)
        for i, (item, item_type) in enumerate(self.menu_options):
            prefix = "> " if i == self.selected_vertical_index else "  "

            if item_type == "selector":
                val = self.selectors_data[item][self.selectors_indexes[item]][0]
                if val == "white" and self.theme == "light":
                    val = "black"
                text = f"{item}: < {val} >"
            else:
                text = f"{item}"

            x =  2

            menu_win.addstr(i + 2, x, prefix, curses.A_BLINK | (curses.A_REVERSE if i == self.selected_vertical_index else curses.A_NORMAL))
            menu_win.addstr(i + 2, x + 2, text, curses.A_REVERSE | curses.A_BOLD if i == self.selected_vertical_index else curses.A_NORMAL)

    def parse_coords(self, input_str : str) -> tuple:
        try:
            parts = input_str.split(',')
            
            if len(parts) != 2:
                return (-1, -1)
            
            x = int(parts[0].strip())
            y = int(parts[1].strip())
            if (x, y) in (self.config["entry"], self.config["exit"]):
                return (-1, -1)
            elif x >= self.config["width"] or y >= self.config["height"]:
                return (-1, -1)
            elif x < 0 or y < 0:
                return (-1, -1)
            
            return (x, y)
        except (ValueError, AttributeError):
            return (-1, -1)

    def parse_input_box(self) -> None:
        input = self.input_box.gather().strip()
        if self.input_come_from == "seed" and input == "random":
            self.config[self.input_come_from] = None
        elif self.input_come_from in ("width", "height") and input.isdecimal():
            self.config[self.input_come_from] = int(input)
        elif self.input_come_from in ("entry", "exit") and self.parse_coords(input) != (-1, -1):
            self.config[self.input_come_from] = tuple(self.parse_coords(input))
        else:
            curses.flash()


    def handle_input_box(self) -> None:
        self.parse_input_box()


        self.config_menu = {
            (f"width : {self.config["width"]}", "button") : self.width_config_button,
            (f"height : {self.config["height"]}", "button") : self.height_config_button,
            (f"entry : {self.config["entry"]}", "button") : self.entry_config_button,
            (f"exit : {self.config["exit"]}", "button") : self.exit_config_button,
            (f"seed : {self.config["seed"] if self.config["seed"] else "random"}", "button") : self.seed_config_button,
            (f"perfect ", "selector") : None,
            ("back", "button") : self.back_to_main_menu,
        }
        self.menu_options = self.config_menu

    def handle_menu_input(self) -> str | None:

        menu_options = list(self.menu_options.keys())
        current_name, current_type = menu_options[self.selected_vertical_index]
        curses.set_escdelay(1)

        if not self.maze_is_animating and not self.path_is_animating:
            self.menu_win.nodelay(False)
            self.input_win.nodelay(False)
        else:
            self.menu_win.nodelay(True)
            self.input_win.nodelay(True)

        try:
            key = self.menu_win.getch()
        except curses.error:
            return None


        if self.input_mod:
            self.sub_input_win.leaveok(True)
            if key in (10, 13, 7):
                self.input_mod = False
                self.input_panel.hide()
                self.input_done = True
                self.handle_input_box()
            else:
                self.input_box.do_command(key)
            return None

        if key == curses.KEY_UP or key == ord('k'):
            self.selected_vertical_index = (self.selected_vertical_index - 1) % len(self.menu_options)

        if key == curses.KEY_DOWN or key == ord('j'):
            self.selected_vertical_index = (self.selected_vertical_index + 1) % len(self.menu_options)

        if current_type == "selector":
            if key in [curses.KEY_LEFT, ord('h')]:
                self.selectors_indexes[current_name] = (self.selectors_indexes[current_name] - 1) % len(self.selectors_data[current_name])
            elif key in [curses.KEY_RIGHT, ord('l')]:
                self.selectors_indexes[current_name] = (self.selectors_indexes[current_name] + 1) % len(self.selectors_data[current_name])

        else:
            if key in [curses.KEY_ENTER, ord('\n')]:
                return menu_options[self.selected_vertical_index][0]

        if key == ord(' '):
            self.togle_animation = not self.togle_animation

        if key == ord('?'):
            self.show_help()

        if key == 27:
            self.back_to_main_menu()

        return None


    def random_maze_animation(self) -> list:
        maze = self.maze
        coords = [(x, y) for y in range(maze.height,) for x in range(maze.width)]

        self.maze_animation_step_number = 5

        random.shuffle(coords)
        return coords

    def line_by_line_maze_animation(self) -> list:
        maze = self.maze
        coords = [(x, y) for y in range(maze.height,) for x in range(maze.width)]

        self.maze_animation_step_number = self.maze.width

        return coords

    def cell_by_cell_maze_animation(self) -> list:
        maze = self.maze
        coords = [(x, y) for y in range(maze.height,) for x in range(maze.width)]

        self.maze_animation_step_number = 1

        return coords


    def prim_maze_animation(self):
        maze = self.maze
        self.maze_animation_step_number = 1
        start_node = maze.entry_point
        order = []
        visited = {start_node}
        frontier = [start_node]

        while frontier:
            current = random.choice(frontier)
            frontier.remove(current)

            order.append(current)
            cx, cy = current
            cell = maze.grid.get_cell(cx, cy)

            for direction, (dx, dy) in [("N", (0, -1)), ("S", (0, 1)), ("W", (-1, 0)), ("E", (1, 0))]:
                nx, ny = cx + dx, cy + dy

                if 0 <= nx < maze.width and 0 <= ny < maze.height:
                    if (nx, ny) not in visited and cell.walls[direction]:
                        visited.add((nx, ny))
                        frontier.append((nx, ny))

        return order


    def oil_effect_maze_animation(self):
        maze = self.maze
        self.maze_animation_step_number = 5
        cx, cy = maze.width // 2, maze.height // 2

        coords = []
        for y in range(maze.height):
            for x in range(maze.width):
                distance = max(abs(x - cx), abs(y - cy))
                coords.append((x, y, distance))

        coords.sort(key=lambda c: c[2])

        return [(c[0], c[1]) for c in coords]


    def spread_maze_animation(self):
        maze = self.maze
        self.maze_animation_step_number = 2
        start_node = (maze.width // 2, maze.height // 2)
        order = []

        queue = deque([start_node])
        visited = {start_node}

        order.append(start_node)

        while queue:
            cx, cy = queue.popleft()
            cell = maze.grid.get_cell(cx, cy)

            for direction, (dx, dy) in [("N", (0, -1)), ("S", (0, 1)), ("W", (-1, 0)), ("E", (1, 0))]:
                nx, ny = cx + dx, cy + dy

                if 0 <= nx < maze.width and 0 <= ny < maze.height:
                    if (nx, ny) not in visited and cell.walls[direction]:
                        visited.add((nx, ny))
                        queue.append((nx, ny))
                        order.append((nx, ny))

        return order


    def prepare_maze_timeline(self):
        self.maze_timeline = []

        maze = self.maze
        maze = self.maze

        self.current_animation = self.selectors_data["animation"][self.selectors_indexes["animation"]][0]
        coords = self.maze_animation_types[self.current_animation]() 
        for x, y in coords:
            cell = maze.grid.get_cell(x, y)

            real_x = (x * 2) + 1
            real_y = (y * 2) + 1

            actions = [(real_y, real_x)]

            if cell.walls["N"]: actions.append((real_y - 1, real_x))
            if cell.walls["S"]: actions.append((real_y + 1, real_x))
            if cell.walls["W"]: actions.append((real_y, real_x - 1))
            if cell.walls["E"]: actions.append((real_y, real_x + 1))

            self.maze_timeline.append(actions)


    def animate_maze(self) -> None:
        delay : float = 0.06 
        if not self.maze_is_animating:
            return
        elif self.togle_animation == False:
            self.maze_animation_step = len((self.maze_timeline))

        current_time = time.time()

        if current_time - self.last_time_maze_animation >= delay:

            if self.maze_animation_step < len(self.maze_timeline):
                self.maze_animation_step += self.maze_animation_step_number
                self.last_time_maze_animation = current_time

            else:
                self.maze_is_animating = False
                self.INITIAL_STATE = False


    def animate_path(self) -> None:
        delay : float = 0.03
        if not self.path_is_animating or self.maze_is_animating:
            return

        current_time = time.time()

        if current_time - self.last_time_path_animation >= delay:

            if self.path_animation_step < len(self.path):
                self.path_animation_step += 1
                self.last_time_path_animation = current_time

            else:
                self.path_is_animating = False



    def draw_path(self) -> None:
        if self.path_shown == False or self.INITIAL_STATE == True:
            return
        maze_win = self.maze_win
        maze = self.maze

        path = self.path

        start_x = (self.maze_width - (maze.width * 2 + 1)) // 2
        start_y = 2
        cell_char = "█"
        path_color = self.selectors_data["path color"][self.selectors_indexes["path color"]][1]
        path_color = (self.selectors_data["walls color"][self.selectors_indexes["walls color"]][1] + 3) % 7

        entry_x, entry_y = maze.entry_point
        exit_x, exit_y = maze.exit_point

        entry_x = start_x + (entry_x) * 2 + 1
        entry_y = start_y + (entry_y) * 2 + 1

        exit_x = start_x + (exit_x) * 2 + 1
        exit_y = start_y + (exit_y) * 2 + 1

        for i, dir in enumerate(path):
            if i >= self.path_animation_step and self.path_is_animating:
                break
            if dir == "N":
                maze_win.addstr(entry_y, entry_x, cell_char, curses.color_pair(path_color))
                maze_win.addstr(entry_y - 1, entry_x, cell_char, curses.color_pair(path_color))
                entry_y -= 2
            if dir == "S":
                maze_win.addstr(entry_y, entry_x, cell_char, curses.color_pair(path_color))
                maze_win.addstr(entry_y + 1, entry_x, cell_char, curses.color_pair(path_color))
                entry_y += 2
            if dir == "W":
                maze_win.addstr(entry_y, entry_x, cell_char, curses.color_pair(path_color))
                maze_win.addstr(entry_y, entry_x - 1, cell_char, curses.color_pair(path_color))
                entry_x -= 2
            if dir == "E":
                maze_win.addstr(entry_y, entry_x, cell_char, curses.color_pair(path_color))
                maze_win.addstr(entry_y, entry_x + 1, cell_char, curses.color_pair(path_color))
                entry_x += 2

        # print(maze.solve(), file=sys.stderr)



    def draw_maze(self) -> None:
        maze_win = self.maze_win
        maze = self.maze

        start_x = (self.maze_width - (maze.width * 2 + 1)) // 2
        start_y = 2
        cell_char = "█"
        maze_win.erase()
        maze_win.box()

        cell_color = self.selectors_data["walls color"][self.selectors_indexes["walls color"]][1]

        entry_x, entry_y = maze.entry_point
        exit_x, exit_y = maze.exit_point

        entry_x = start_x + (entry_x) * 2 + 1
        entry_y = start_y + (entry_y) * 2 + 1

        exit_x = start_x + (exit_x) * 2 + 1
        exit_y = start_y + (exit_y) * 2 + 1

        for y in range(maze.height * 2 + 1):
            for x in range(maze.width * 2 + 1):
                if x % 2 == 0 or y % 2 == 0:
                    maze_win.addstr(start_y + y, start_x + x, cell_char, curses.color_pair(cell_color))
                else:
                    maze_win.addstr(start_y + y, start_x + x, ' ')

        for i in range(min(self.maze_animation_step, len(self.maze_timeline))):
            cell_actions = self.maze_timeline[i]
            for (rel_y, rel_x) in cell_actions:
                maze_win.addstr(start_y + rel_y, start_x + rel_x, " ")

        path_color = self.selectors_data["path color"][self.selectors_indexes["path color"]][1]
        maze_win.addstr(entry_y, entry_x, cell_char, curses.color_pair((cell_color + 2) % 7))
        maze_win.addstr(exit_y, exit_x, cell_char, curses.color_pair((cell_color + 1)%7))

        animation_togle_fieald = f"[animation {self.togle_animation}]"
        seed_fieald = f"[seed={maze.seed}]"
        self.maze_win.addstr(self.maze_height - 1, 1, f"infos:")
        self.maze_win.addstr(self.maze_height - 1, 8, animation_togle_fieald, curses.color_pair(3) | curses.A_BOLD)
        self.maze_win.addstr(self.maze_height - 1, len(animation_togle_fieald) + 9, seed_fieald, curses.color_pair(3))


    def exit_programme(self) -> None:
        exit(0)


    def back_to_main_menu(self) -> None:
        self.menu_state = "main"
        self.menu_options = self.main_menu
        self.selected_vertical_index = 0


    def open_config_menu(self) -> None:
        self.menu_state = "(config menu):"
        self.menu_options = self.config_menu
        self.selected_vertical_index = 0


    def generate(self) -> None:
        # if not self.INITIAL_STATE:
        self.maze = MazeGenerator(
            self.config["width"],
            self.config["height"],
            self.config["seed"],
            self.selectors_data["perfect "][self.selectors_indexes["perfect "]][1],
            self.config["entry"],
            self.config["exit"],
        )
        self.maze_animation_step = 0
        self.path_animation_step = 0
        if self.togle_animation:
            self.path_shown = False
        self.maze_is_animating = True
        self.path = self.maze.solve()

        self.prepare_maze_timeline()

    def show_path(self) -> None:
        if self.maze_is_animating:
            return

        self.path = self.maze.solve()
        self.path_shown = not self.path_shown
        self.path_is_animating = True
        self.path_animation_step = 0


    def open_animation_menu(self) -> None: 
        self.menu_state = "(custom options)"
        self.menu_options = self.customization_menu
        self.selected_vertical_index = 0


    def menu(self) -> None:
        if self.error_mod or not self.handle_menu_input():
            return

        keys = list(self.menu_options.keys())

        current_key = keys[self.selected_vertical_index]

        menu_func = self.menu_options.get(current_key)

        if menu_func:
            menu_func()


    def check_isresized(self) -> bool:
        y, x = self.stdscr.getmaxyx()
        if y != self.scr_height or x != self.scr_width:
            return True
        return False


    def resize_windows(self) -> None:
        try:
            y, x = self.stdscr.getmaxyx()
            self.scr_height, self.scr_width = y, x
            curses.resizeterm(y, x)
            curses.update_lines_cols()

            self.stdscr.clear()
            self.stdscr.box()
            self.create_maze()
            self.create_menu()
            self.create_input_popup("")
            self.create_help()
            self.create_error_popup()
        except curses.error:
            self.create_error_popup()



BLACK = 0
RED = 1
GREEN = 2
YELLOW = 3
BLUE = 4
MAGENTA = 5
CYAN = 6
WHITE = 8

def display(stdscr : CWindow, maze : Maze) -> None:

    displayer : Display = Display(maze, stdscr)
    displayer.prepare_maze_timeline()

    while True:

        displayer.theme = displayer.selectors_data["theme"][displayer.selectors_indexes["theme"]][0]
        if displayer.theme == "dark":
            curses.init_pair(1, WHITE, -1)
            curses.init_pair(2, CYAN, -1)
            curses.init_pair(3, BLUE, -1)
            curses.init_pair(4, GREEN, -1)
            curses.init_pair(5, RED, -1)
            curses.init_pair(6, YELLOW, -1)
            curses.init_pair(7, MAGENTA, -1)
        else:
            curses.init_pair(1, BLACK, WHITE)
            curses.init_pair(2, CYAN, WHITE)
            curses.init_pair(3, BLUE, WHITE)
            curses.init_pair(4, GREEN, WHITE)
            curses.init_pair(5, RED, WHITE)
            curses.init_pair(6, YELLOW, WHITE)
            curses.init_pair(7, MAGENTA, WHITE)


        if not displayer.error_mod:
            displayer.popup_panel.hide()
            displayer.show_maze()
            displayer.show_menu()
            displayer.animate_maze()
            displayer.animate_path()
        else:
            displayer.show_error_popup()

        try:
            displayer.draw_maze()
            displayer.draw_path()
            displayer.draw_menu()


            displayer.error_mod = False

        except (AttributeError, curses.error):
            displayer.error_mod = True

        if displayer.check_isresized():
            displayer.resize_windows()

        curses.panel.update_panels()
        curses.doupdate()
        displayer.menu()
        curses.napms(30)


def main() -> None:
    """Entry point for the maze generator program.

    Reads the configuration file path from command-line arguments,
    validates it, generates a maze, and prints the solution path.

    Raises:
        InvalidArgumentError: If the wrong number of arguments is provided.
        InvalidFileError: If the config file has an invalid extension.
        InvalidEntryError: If the config file contains invalid entries.
    """
    try:
        if len(sys.argv) != 2:
            raise InvalidArgumentError(
                "Usage: python3 a_maze_ing.py config.txt"
            )

        filename: str = sys.argv[1]
        _, extension = os.path.splitext(filename)

        if extension != ".txt":
            raise InvalidFileError(
                "Configuration file must be plain text (e.g. config.txt)."
            )

        config: Dict[str, Any] = validate(filename)

        maze = MazeGenerator(
            width=config['WIDTH'],
            height=config['HEIGHT'],
            seed=config['SEED'],
            perfect=config['PERFECT'],
            entry_point=config['ENTRY'],
            exit_point=config['EXIT']
        )

        maze_writer = MazeWriter(maze, config["OUTPUT_FILE"])
        maze_writer.write()
        curses.wrapper(display, maze)

    except (InvalidEntryError, InvalidFileError, InvalidArgumentError) as e:
        print(f"ERROR: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
