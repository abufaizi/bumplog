
# User Interface (UI)
#   Used to print to the console


# Local Modules
import info

# NonLocal Modules
import subprocess
import curses


def terminal_dimensions():
    rows, cols = subprocess.check_output(['stty', 'size']).split()
    return (cols, rows)

def clear_screen(win):
    # Clears the screen for screen to be printed on
    win.clear()

def refresh_screen(win):
    win.refresh()

# TEST METHOD
def get_category(position):
    # Start from 2nd to last character in position string and move
    #  backwards to find the next '/'
    category = ''
    for i in range(0, len(position) - 1):
        if position[-(i+1)] == '/':
            return position[-i:-1]
        elif i == (len(position) + 1):
            return position[:-1]

def print_header(win, wdth, x, position, name):
    category = ''
    for i in range(0,len(position) - 1):
        if position[-(i+1)] == '/':
            category = position[-i:-1]
            break
        elif i == len(position) + 1:
            category = position[:-1]
            break
    category = category[0].upper() + category[1:]
    new_line(win)
    #2nd Line Beginning
    if x <= wdth + 4:
        mrgn = 1
    else:
        mrgn = 2
    win.addstr(' ' * mrgn + category + ' ' * (x-len(category)-len(name)-(mrgn*2)) + name)
    new_line(win)
    #3rd Line Beginning
    new_line(win)
    #4th Line Beginning


def print_left(win, section, wdth, mrgn):
    lines = parse_lines(section, wdth)
    for i in range(0, len(lines)):
        win.addstr(' ' * mrgn + lines[i])
        if i < len(lines) - 1:
            new_line(win)

def print_center(win, section, wdth, x, switch):
    lines = parse_lines(section, wdth)
    for i in range(0, len(lines)):
        win.addstr(' ' * int((x-len(lines[i]))/2))
        if x % 2 != len(lines[i]) % 2:
            if i < len(lines) - 1:
                if switch == True:
                    switch = False
                else:
                    win.addstr(' ')
                    switch = True
        win.addstr(lines[i])
        if i < len(lines) - 1:
            new_line(win)

def print_right(win, section, wdth, mrgn):
    lines = parse_lines(section, wdth)
    for i in range(0, len(lines)):
        win.addstr(' ' * (mrgn + (wdth - len(lines[i]))))
        if i == len(lines) - 1:
            win.addstr(' ' + lines[i])
        else:
            win.addstr(lines[i])
            new_line(win)


def highlight_left(win, section, wdth, mrgn):
    lines = parse_lines(section, wdth)
    for i in range(0, len(lines)):
        win.addstr(' ' * mrgn)
        win.addstr(lines[i], curses.A_STANDOUT)
        if i < len(lines) - 1:
            new_line(win)

def highlight_center(win, section, wdth, x, switch):
    lines = parse_lines(section, wdth)
    for i in range(0, len(lines)):
        win.addstr(' ' * int((x-len(lines[i]))/2))
        if x % 2 != len(lines[i]) % 2:
            if i < len(lines) - 1:
                if switch == True:
                    switch = False
                else:
                    win.addstr(' ')
                    switch = True
        win.addstr(lines[i], curses.A_STANDOUT)
        if i < len(lines) - 1:
            new_line(win)

def highlight_right(win, section, wdth, mrgn):
    lines = parse_lines(section, wdth)
    for i in range(0, len(lines)):
        win.addstr(' ' * (mrgn + (wdth - len(lines[i]))))
        if i == len(lines) - 1:
            win.addstr(' ')
            win.addstr(lines[i], curses.A_STANDOUT)
        else:
            win.addstr(lines[i], curses.A_STANDOUT)
            new_line(win)




def print_divider(win, x):
    win.addstr('  ' + '-' * (x - 4))
    new_line(win)
    new_line(win)






# Print Procedures --------------------------------------------------- #

def parse_lines(section, wdth):
    # Returns a list of each line with the respect to the lines width
    lines = []
    while True:
        hyphen = False
        if len(section) <= wdth:
            lines.append(section)
            if len(section) == wdth:
                lines.append('')
            break
        else:
            line = ''
            r_indx = -1
            l_indx = -1
            if section[wdth] != ' ':
                cnt = 1
                hit = False
                while True:
                    if section[wdth - cnt] == ' ':
                        if r_indx == -1:
                            r_indx = wdth - cnt + 1
                        hit = True
                        cnt += 1
                    elif hit: # and section[wdth - cnt] != ' '
                        l_indx = wdth - cnt + 1
                        break
                    elif cnt == wdth:
                        l_indx = wdth - 1
                        r_indx = wdth - 1
                        hyphen = True
                        break
                    else:
                        cnt += 1
            else:
                if len(section) > wdth+1:
                    if section[wdth - 1] != ' ' and section[wdth + 1] != ' ':
                        if len(section) > wdth + 1:
                            r_indx = wdth + 1
                        else:
                            r_indx = wdth
                    else:
                        r_indx = wdth
                else:
                    r_indx = wdth
                cnt = 1
                while True:
                    if section[wdth - cnt] != ' ':
                        l_indx = wdth - cnt + 1
                        break
                    else:
                        cnt += 1
            line = section[:l_indx]
            section = section[r_indx:]
            if hyphen:
                line += '-'
            lines.append(line)
    return lines

def new_line(win):
    win.addstr('\n')

# --------------------------------------------------- Print Procedures #


# Copyright 2017 Neil Graham
