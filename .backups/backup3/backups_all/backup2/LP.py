
# Logical Procedures (LP)
#    Used for executing general purpose logical procedures


# Local Modules
import FM

# NonLocal Modules
import random


def weight_conv(bump):
    return (10*bump)**(1/2)+1

def total_weight(logs_all):
    # Returns the total weight of all positional logs
    weight_all = 0
    for i in range(0, len(logs_all)):
        weight_all += weight_conv(logs_all[i][1])
    return weight_all

# ---------------- #

def hor_info(x, max_wdth):
    wdth = 0
    mrgn = 0
    if x > max_wdth + 4:
        if (x % 2) == 0:
            wdth = max_wdth
            mrgn = int((x - wdth) / 2)
        elif x % 2 == 1:
            wdth = max_wdth+1
            mrgn = int((x - wdth) / 2)
    else:
        wdth = x - 4
        mrgn = 2
    return wdth, mrgn

# ----------------- #

def choosewrt_weight(logs_all, weight_all):
    rand_num = random.randint(0, weight_all)
    num = 0
    for i in range(0, len(logs_all)):
        num += logs_all[i][1]
        if num > rand_num:
            return i - 1
    return len(logs_all) - 1
