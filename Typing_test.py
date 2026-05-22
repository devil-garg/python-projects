import curses
from curses import wrapper
import time

def start_screen(stdscr) :
    stdscr.clear()
    stdscr.addstr("Welcome to the Speed Typing Test!")
    stdscr.addstr("\nPress any key to begin!")
    stdscr.refresh()
    stdscr.getkey()

def wpm_test(stdscr) :
    target_text = "Hello man, this is your typing speed test and with corresponding words thorough zebra crossing will be crossed"
    current_text = []
    start_time = time.time()
    stdscr.nodelay(True) # program doesnt stop waiting for an input but now getkey() throws an exception if user doesnt type

    while True :
        stdscr.clear()
        stdscr.addstr(1,0,target_text,curses.color_pair(3))
        elapsed_time = max(0, time.time() - start_time) # Ensure time doesn't go negative if system clock changes
        stdscr.addstr(2, 0, f"Time: {round(elapsed_time, 2)}s")
        for index, char in enumerate(current_text) :
            if target_text[index] == char :
                stdscr.addstr(1, index, char, curses.color_pair(1))
            else :
                stdscr.addstr(1, index, char, curses.color_pair(2))

        stdscr.refresh()

        try :
            key = stdscr.getkey()
        except :
            continue

        if key == "\x1b" :
            break
        elif key in ("KEY_BACKSPACE", "\b", "\x7f") :
            if len(current_text) > 0 :
                current_text.pop()
        elif len(current_text) == len(target_text) and "".join(current_text) == target_text : #joins the characters in the list by string mention as "" eg "-" ->h-e-l-l-o
                break
        elif len(key) == 1:
                current_text.append(key)
    
    time.sleep(5)

def main(stdscr) :
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED,curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE,curses.COLOR_BLACK)
    start_screen(stdscr)
    wpm_test(stdscr)

wrapper(main)
