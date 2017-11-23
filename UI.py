
# User Interface (UI)
#   Used to print to the console


# NonLocal Modules
import os
import subprocess


#Text will only be up to 65 characters wide
#If terminal width is odd, up to 65 characters wide
# Margin on each side will be (term width - 65) / 2

#If terminal width is even, up to 64 characters wide
# Margin on each side will be (term width - 64) / 2


def clear_screen():
    # Clears the screen for screen to be printed on
    os.system('clear')

def terminal_dimensions():
    rows, cols = subprocess.check_output(['stty', 'size']).split()
    return (cols, rows)

def print_header(x, category, name):
    print()
    print(' ' + category + ' ' * (x-len(category)-len(name)-2) + name + ' ')
    print()

def print_log(log, width, margin):
    log = log.split()
    line_length = 0
    line_words = []
    for word in log:
        if (line_length + len(word)) > width:
            # If next word goes over line length, print entire line_width
            print_line(line_words, width, margin)
            line_length = 0
            line_words = []
        line_length += len(word) + 1
        line_words.append(word)
    print_line(line_words, width, margin)

def print_line(words, width, margin):
    print(' ' * margin, end='')
    for word in words:
        print(word + ' ', end='')
    print()

def print_footer(x):
    print('-' * x)
    print()


# Copyright 2017 Neil Graham
