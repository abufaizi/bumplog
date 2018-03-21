
# 2nd Iteration of Logical Procedures (LP2)
#    Used for executing general logical procedures


# Local Modules
import FM

# NonLocal Modules
import datetime
import random
import math


def weight(bump):
    return (10*bump)**(1/2)+1

def total_weight(logs_bumps):
    # Returns the total bump count for all chosen logs
    weight_all = 0
    for i in range(0, len(logs_bumps)):
        weight_all += weight(logs_bumps[i][1])
    return weight_all


def hor_info(x, max_wdth):
    wdth = 0
    mrgn = 0

    if x > max_wdth + 4:
        if (x % 2) == 0:
            wdth = max_wdth
        else:
            wdth = max_wdth + 1
        mrgn = int((x - wdth) / 2)
    else:
        wdth = x - 4
        mrgn = 2

    return wdth, mrgn


def section_height(section, wdth):
    # Returns the height of a string of words. Empty string height == 1.
    height = 1
    while True:
        if len(section) <= wdth:
            if len(section) == wdth:
                height += 1
            break
        else:
            line = ''
            r_indx = -1
            if section[wdth] != ' ':
                cnt = 1
                hit = False
                while True:
                    if section[wdth - cnt] == ' ':
                        r_indx = wdth - cnt + 1
                        break
                    elif cnt == wdth:
                        r_indx = wdth - 1
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
            section = section[r_indx:]
            height += 1
    return height


def choose_wrt_weight(logs, total_bumps):
    # Returns an index with respect to bump count
    rand_num = random.randint(0, total_bumps)
    num = 0
    for i in range(0, len(logs)):
        num += logs[i][1]
        if num > rand_num:
            return i - 1
    return -1

# Copyright 2018 Neil Graham
