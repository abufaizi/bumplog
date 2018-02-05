
import LP
import UI
import FM

import datetime
import random
import math

def review(content):
    # Keep track of all logs shown and show logs w/ respect to bumps,
    # given list of all (logs, bumps, dates)
    logs = LP.setup_logs()
    all_bumps = LP.total_bumps(logs)
    logs_chosen = []
    typed = ''
    #While loop would be here
    log_end = 0
    x, y = UI.terminal_dimensions()
    x, y = int(x), int(y)
    width, margin = LP.ui_width(x)
    y_left = y - 6
    complete = False
    if len(typed) != 0:
        y_left -= 1 - LP.log_height(typed, width)
    else:
        y_left -= 2
    for i in range(0, len(logs_chosen)):
        y_new = y_left - 1 - LP.log_height(FM.get_subsring('logs', logs_chosen), width)
        if y_new < 0:
            log_end = i+1
            complete = True
            break
        elif y_new == 0 and len(logs_chosen) > i:
            log_end = i + 1
            complete = True
            break
        else:
            y_left = y_new
    if not complete:
        while True:
            print('Logs B:')
            print(logs)
            print()
            print('AllBumps B: ' + str(all_bumps))
            print()
            print('LogsChosen B: ', end='')
            print(logs_chosen)
            print()
            rand_num = LP.random_log(logs, all_bumps)
            print('RandNum: ' + str(rand_num))
            print()
            log_item = logs.pop(rand_num)
            print('LogItem: ', end='')
            print(log_item)
            print()
            print('Logs A:')
            print(logs)
            print()
            all_bumps -= log_item[1]
            print('AllBumps A: ' + str(all_bumps))
            print()
            logs_chosen.append(log_item[0])
            print('LogsChosen A: ', end='')
            print(logs_chosen)
            print()
            print('-' * x)
            y_new = y_left - 1 - LP.log_height(FM.get_substring('logs', log_item[0]), width)
            if y_new < 0:
                log_end = len(logs_chosen)
                break
            else:
                y_left = y_new

'''
if not complete:
    while True:
        rand_num = LP.random_log(logs, all_bumps)
        log_item = logs.pop(rand_num)
        all_bumps -= log_item[1]
        logs_chosen.append(log_item[0])
        y_new = y_left - 1 - LP.log_height(FM.get_substring('logs', log_item[0]), width)
        if y_new < 0:
            log_end = len(logs_chosen)
            break
        else:
            y_left = y_new
'''


	# while True:
	# 	key = ''
	# 	log_end = 0
	# 	x, y = UI.terminal_dimensions()
	# 	x, y = int(x), int(y)
	# 	width, margin = LP.ui_width(x)
	# 	y_left = y - 6
	# 	complete = False
	# 	if len(typed) != 0:
	# 		y_left -= 1 - LP.log_height(typed, width)
	# 	else:
	# 		y_left -= 2
	# 	for i in range(0, len(logs_chosen)):
	# 		y_new = y_left - 1 - LP.log_height(FM.get_substring('logs', logs_chosen[i]), width)
	# 		if y_new < 0:
	# 			log_end = i
	# 			complete = True
	# 			break
	# 		elif y_new == 0 and len(logs_chosen) > i:
	# 			log_end = i+1
	# 			complete = True
	# 			break
	# 		else:
	# 			y_left = y_new
	# 	if not complete:
	# 		while True:
	# 			rand_num = LP.random_log(logs, all_bumps)
	# 			print(rand_num)
	# 			log_item = logs[rand_num]
    #             del logs[rand_num]
	# 			all_bumps -= log_item[1]
	# 			logs_chosen.append(log_item[0])
	# 			y_new = y_left - 1 - LP.log_height(FM.get_substring('logs', log_item[0]), width)
	# 			if y_new < 0:
	# 				log_end = len(logs_chosen)
	# 				break
	# 			else:
	# 				y_left = y_new
	# 	for i in range(0, math.ceil(y_left/2)):
	# 		# Print Upper Margins
	# 		y_left -= 1
	# 	for i in range(0, log_end):
	# 		# Print All Logs
	# 		log = FM.get_substring('logs', logs_chosen[i])
	# 	for i in range(0, y_left):
	# 		# Print Lower Margins
	# 		y_left -= 1


review(LP.all_content())
