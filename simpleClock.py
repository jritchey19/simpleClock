#!/usr/bin/env python3 

'''A simple curses clock to learn on.'''

import curses
from curses import wrapper
from datetime import datetime
from time import sleep

def main(stdscr):
    '''
    Main portion of script that starts 
    by getting time from the local host.
    Then refreshes the seconds to increment
    by one.
    '''
    # Make stdscr.getch non-blocking.
    curses.curs_set(0)
    curses.start_color()

    # Need to initialize color first before it can be used.
    # Must have a number, a foreground, and a background.
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(4, curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_color(5, 1000, 0, 0)
    curses.init_color(6, 0, 0, 0)
    curses.init_pair(5, 5, curses.COLOR_BLACK)

    y,x = stdscr.getmaxyx()  # Get the terminals screen's size.
    stdscr.nodelay(True)
    stdscr.clear()  # Clear the screen initially.

    # Get the time from the host machine.
    sec = datetime.now().second
    minute = datetime.now().minute
    hour = datetime.now().hour

    # Start a loop.
    while True:
        c = stdscr.getch()
        curses.flushinp()
        stdscr.erase()  # Deal with the flicker on the screen.
        # Press q to exit.
        if c == ord('q'):
            break
        # Draw Clock bars to the screen.
        stdscr.addstr(
            0,  # Y coordinate.
            0,  # X coordinate.
            "#" * sec,  # String to print to screen. 
            curses.color_pair(2)  # attribute.
        )

        # Try with custom colors.
        stdscr.addstr(
            1,
            0,
            "#" * minute, 
            curses.color_pair(5)
        )

        # Make string the color blue and bold.
        stdscr.addstr(
            2,
            0,
            "#" * hour, 
            curses.color_pair(4) | curses.A_BOLD  
        )
        stdscr.addstr(
            3,
            0,
            "=" * x, 
            curses.color_pair(1)
        )

        # If digits are under 10, add a zero in front to make everything
        # 24-hour time.
        if sec < 10:
            dsec = "0" + str(sec)
        else:
            dsec = str(sec)
        if minute < 10:
            dminute = "0" + str(minute)
        else:
            dminute = str(minute)
        if hour < 10:
            dhour = "0" + str(hour)
        else:
            dhour = str(hour)

        stdscr.addstr(
            4,
            0, 
            f"Time:[{dhour}:{dminute}:{dsec}]", 
            curses.color_pair(1)
        )
        stdscr.addstr(
            5,
            0,
            "Press q to quit.", 
            curses.color_pair(1)
        )
        # Use time from the server.
        sec = datetime.now().second
        minute = datetime.now().minute
        if minute == 59:
            lasMin = True
        hour = datetime.now().hour

        #  Got chime?
        if minute == 0:
            if lasMin:
                for h in range(0, hour):
                    curses.flash()
                    sleep(0.1)  # Wait for a brief moment.
                lasMin = False

        stdscr.refresh()  # Refresh only the parts that change on screen.
        # Wait 1/100 of a second. 
        sleep(0.01)

if __name__ == '__main__':
    wrapper(main)
