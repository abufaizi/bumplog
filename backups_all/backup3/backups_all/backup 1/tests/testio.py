
import curses

def main(win):
    win.nodelay(True)
    key = ''
    record = ''
    win.clear()
    win.addstr("Key:")
    win.addstr('\n\nRecord:')
    win.addstr(record)
    while True:
        try:
            key = win.getkey()

            if str(key) == '^?':
                # Attempt at detecting the Backspace key
                record = record[:-1]

            elif str(key) == '\n':
                # Attempt at detecting the Enter Key
                record = ''

            else:
                record += str(key)
            win.clear()
            win.addstr("Key:")
            win.addstr(str(repr(key)))
            win.addstr('\n\nRecord:')
            win.addstr(record)
            if key == os.linesep:
                break
        except Exception as e:
            # No input
            pass

curses.wrapper(main)
# CTRL+C to close the program
