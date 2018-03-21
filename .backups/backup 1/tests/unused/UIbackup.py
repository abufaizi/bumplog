def first_print_section(win, section, wdth, mrgn):
    section = section.split()
    line_length = 0
    line_words = []
    for word in section:
        if (line_length + len(word)) > wdth:
            # If next word goes over line length, print entire line_wdth
            print_line(win, line_words, wdth, mrgn)
            new_line(win)
            line_length = 0
            line_words = []
        line_length += len(word) + 1
        line_words.append(word)
    print_line(win, line_words, wdth, mrgn)

def print_line(win, words, wdth, mrgn):
    win.addstr(' ' * mrgn)
    for word in words:
        win.addstr(word + ' ')

def print_section(win, section, wdth, mrgn):
    #words_all = section.split()
    while True:
        hyphen = False
        if len(section) <= wdth:
            win.addstr(' ' * mrgn + section)
            if len(section) == wdth:
                new_line(win)
                win.addstr(' ' * mrgn)
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
            win.addstr(' ' * mrgn + line)
            new_line(win)

def highlight_left(win, section, wdth, mrgn):
    #words_all = section.split()
    while True:
        hyphen = False
        if len(section) <= wdth:
            win.addstr(' ' * mrgn)
            win.addstr(section, curses.A_STANDOUT)
            if len(section) == wdth:
                new_line(win)
                win.addstr(' ' * mrgn)
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
            win.addstr(' ' * mrgn)
            win.addstr(line, curses.A_STANDOUT)
            new_line(win)
