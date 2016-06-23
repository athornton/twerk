#!/usr/bin/env python
import curses
import time
import argparse
 
def _get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-x', '--xxx',
                        required=False,
                        action='store_true',
                        help='bottomless')
    args = parser.parse_args()
    return args
 
def main(screen):
    args=_get_args()
    bottom="Y"
    if "xxx" in args and args.xxx:
        bottom = "."
    delay = 0.3
    twerk = [ " 0%so   " % bottom,
              "  O%sO  " % bottom,
              "   o%s0 " % bottom ]
    curses.start_color()
    height,width = screen.getmaxyx()
    upper = int(height - 3 ) / 2
    left  = int(width  - 7 ) / 2
    nwin = curses.newwin(3,7,upper,left)
    nwin.bkgd(' ',curses.A_REVERSE)
    index=0
    incr=1
    while 1:
        tstr = twerk[index]
        if index == 2:
            incr = -1
        if index == 0:
            incr = 1
        index = index + incr
        nwin.addstr(1,0,tstr,curses.A_REVERSE)
        nwin.refresh()
        time.sleep(delay)
 
try:
    curses.wrapper(main)
except KeyboardInterrupt:
    exit()
