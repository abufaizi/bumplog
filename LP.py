
# Logical Procedures (LP)
#	Used as the backbone for all major calculations


# Local Modules
import FM
import UI
#import KI
import info

# NonLocal Modules
import datetime
import random

# File Procedures ---------------------------------------------------- #

def all_content():
	#Returns list of all content(logs, bumps, dates)
	content = []
	logs = FM.get_all('logs')
	bumps = FM.get_all('bumps')
	dates = FM.get_all('dates')
	for i in range(0, len(logs)):
		content.append((logs[i], bumps[i], dates[i]))
	return content

def index_position(text, index):
	#Returns the position(index1:index2) of an index
	count = 0
	start = 0
	end = 0
	for i in range(0, len(text)-1):
		if text[i:i+2] == '\\n':
			if count == index:
				end = i
				return (start, end)
			count += 1
			if count == index:
				start = i+2
	return -1

# ---------------------------------------------------- File Procedures #





# Interface Procedures ----------------------------------------------- #

def review(content):
	# Keep track of all logs shown and show logs w/ respect to bumps,
	# given list of all (logs, bumps, dates)
	logs = setup_logs()
	total_bumps = total_bumps(logs)
	chosen_logs = []
	while True:
		x, y = UI.terminal_dimensions()
		x, y = int(x), int(y)
		UI.clear_screen()
		UI.print_header(x, info.category(), info.name())
		y_left = y - 7
		for index in chosen_logs:
			y_left -= log_height(FM.get_substring('logs', index[0]))
		while y_left > 0:

			chosen_logs.append(pop_log())
		width, margin = ui_width(x)
		UI.print_log(random_log(all_content()), width, margin)
		print()
		UI.print_footer(x)
		input('  ')

		break
		#WIP

def total_bumps(logs):
	#Returns the total bump count for all logs
	total_bumps = 0
	for i in range(0, len(bumps)):
		total_bumps += int(bumps[i])
	return total_bumps

def setup_logs():
	#Returns the index and bump count of every log
	bumps = FM.get_all('bumps')
	indices = [] * len(bumps)
	for i in range(0, len(indices)):
		indices[i] = i
	logs = lists_to_tuple(indices, bumps)
	return logs

def bump_probability(logs, total_bumps):
	#Returns an index with respect to bump count
	rand_num = random.randint(0, total_bumps)
	num = 0
	for i in range(0, len(logs)):
		num += log[i][1]
		if num > rand_num:
			return log[i-1][0]
	return -1



def insert_logs(logs, entry, width, height):
	#
	written_height = 0
	for log in logs:
		h = log_height(log, width)
		if written_height + h > height:
			return
		written_height += log_height(log, width)



def vert_margin():
	print('Not done')
	return upper_margin, lower_margin


def log_height(log, width):
	#Returns the height of a single log, given the width
	log = log.split()
	line_length = 0
	height = 0
	for word in log:
		if line_length + len(word) > width:
			height += 1
			line_length = 0
		line_length += len(word) + 1
	return height

def ui_width(x):
	length = 0
	margin = 0
	if x > 66:
		if (x % 2) == 0:
			length = 64
			margin = int((x - length) / 2)
		elif x % 2 == 1:
			length = 65
			margin = int((x - length) / 2)
	else:
		length = x - 4
		margin = 2
	return length, margin

# ----------------------------------------------- Interface Procedures #





def lists_to_tuple(list1, list2):
	# Returns a list of tuples containing the two list's values
	tpl = []
	if len(list1) == len(list2):
		for i in range(0, len(list1)):
			tpl.append(list1[i], list2[i])
	else:
		return -1
	return tpl

def new_log(log):
	# Appends log, bump, and time to data files
	FM.append_substring('logs', log + '\\n')
	FM.append_substring('bumps', '3\\n')
	FM.append_substring('dates', current_time() + '\\n')

def random_log(content):
	# Returns any random log, given list of all (logs, bumps, dates)
	log_num = random.randint(0,len(content)-1)
	return content[log_num][0]

def current_time():
	# Returns current time (month/day/year hour:minute)
	now = datetime.datetime.now()
	return(now.strftime('%m/%d/%Y %H:%M'))

def bump(log):
	# Get bump number on single log, then add 1 to it
	index = FM.get_index('logs', log)
	bump = FM.get_substring('bumps', index)
	bump = int(bump) + 1
	FM.edit_substring('bumps', index, bump)

def pair_bump_index():
	# Pair the index of each log with their bump count
	bumps = get_all('bumps')
	bump_index = []
	for i in range(0, len(bumps)):
		bump_index.append((bumps[i], i))
	return bump_index


curses.wrapper(main)

# Copyright 2017 Neil Graham
