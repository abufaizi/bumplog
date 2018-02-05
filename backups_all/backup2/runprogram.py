
# Run Program
#   Used to run the note-taking program


# Local Modules
import review

# NonLocal Modules
import curses



def run(win):
    win.nodelay(True)
    review.main(win)

curses.wrapper(run)


# Copyright 2017 Neil Graham
