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
    # Make stdscr.getch non-blocking
    curses.curs_set(0)
    y,x = stdscr.getmaxyx()
    stdscr.nodelay(True)
    stdscr.clear()
    sec = int(datetime.now().second)
    minute = int(datetime.now().minute)
    hour = int(datetime.now().hour)
    while True:
        c = stdscr.getch()
        curses.flushinp()
        stdscr.clear()
        # Press q to exit
        if c == ord('q'):
            break
        # Draw Clock bars to the screen.
        stdscr.addstr(0,0,"#" * sec)
        stdscr.addstr(1,0,"#" * minute)
        stdscr.addstr(2,0,"#" * hour)
        stdscr.addstr(3,0,"=" * x)

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

        stdscr.addstr(4,0, f"Time:[{dhour}:{dminute}:{dsec}]")
        stdscr.addstr(5,0,"Press q to quit.")

        sec = datetime.now().second
        if sec == 60:
            sec = 0
            minute += 1
        if minute == 60:
            minute = 0
            hour += 1
            for h in hour:
                curses.flash()
        if hour == 24:
            hour = 0

        # Wait 1/100 of a second. 
        sleep(0.01)

if __name__ == '__main__':
    wrapper(main)
