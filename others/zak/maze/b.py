import curses
from time import sleep

def demo(screen : curses.window):
    # Start color functionality (handled by wrapper but good practice to know)
    curses.start_color()

    # Check if the terminal can change color definitions
    r = 0
    g = 0
    b = 0
    while True:
        if curses.can_change_color():
            # Define a custom color (a bright red) with RGB values 0-1000
            # Color number 250 is used to avoid interfering with default colors 0-7
            curses.init_color(250, r, g, b) # Max red, no green/blue

            # Define a color pair (pair number 1) using the custom color as foreground
            # and black as background.
            curses.init_pair(1, 250, curses.COLOR_BLACK)

            # Apply the color pair and print a message
            screen.addstr(5, 5, "This is custom bright text!", curses.color_pair(1))
        else:
            screen.addstr(5, 5, "Terminal does not support changing colors.", curses.A_RED)
        r = (r + 10) % 255
        g = (g + 10) % 255
        b = (b + 10) % 255
        screen.refresh()
        sleep(0.05)


# Use curses.wrapper to handle initialization and cleanup
if __name__ == '__main__':
    curses.wrapper(demo)
