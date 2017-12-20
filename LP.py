
# Logical Procedures (LP)
#	Used for executing general logical procedures


# Local Modules
import FM

# NonLocal Modules
import datetime
import random
import math


# Test Procedures ---------------------------------------------------- #
'''
def class_logs(nclass):


def bump_strength(bump):
	#For attributing a incrementally decreasing strength to bumps
	return (10*bump)**(1/2)+1

def total_strength(logs):
	total = 0
	for i in range(0, len(logs)):
		total += bump_strength(int(logs[i][1]))
	return total

def indx_and_strength():
	logs = []
	bumps = FM.get_all('bumps')
	strength = []
	for i in range(0, len(bumps)):
		strength.append(bump_strength(int(bumps[i][:-1])))
	indices = []
	for i in range(0, len(bumps)):
		indices.append(i)
	logs = lists_to_tuple(indices, bumps)
	return logs
'''

# ---------------------------------------------------- Test Procedures #


  #


# Review Procedures -------------------------------------------------- #

def indx_to_substr(indx_list, file_name):
	#Given a list of indices and file_name, returns a list of substrings
	substr_list = []
	for indx in indx_list:
		substr_list.append(FM.get_substring(file_name, indx))

def total_bumps(logs):
	#Returns the total bump count for all logs
	bumps = 0
	for i in range(0, len(logs)):
		bumps += int(logs[i][1])
	return bumps

def indx_and_bump():
	#Returns the index and bump count of every log
	logs = []
	bumps = FM.get_all('bumps')
	for i in range(0, len(bumps)):
		bumps[i] = int(bumps[i][:-1])
	indices = []
	for i in range(0, len(bumps)):
		indices.append(i)
	logs = lists_to_tuple(indices, bumps)
	return logs

def bump_index(logs, total_bumps):
	#Returns an index with respect to bump count
	rand_num = random.randint(0, total_bumps)
	num = 0
	for i in range(0, len(logs)):
		num += logs[i][1]
		if num > rand_num:
			return i-1
	return -1

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



def hor_info(x, max_width):
	width = 0
	margin = 0
	if x > max_width + 4:
		if (x % 2) == 0:
			width = max_width
			margin = int((x - width) / 2)
		elif x % 2 == 1:
			width = max_width+1
			margin = int((x - width) / 2)
	else:
		width = x - 4
		margin = 2
	return width, margin

# -------------------------------------------------- Review Procedures #


  #


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
	for i in range(0, len(text)):
		if text[i] == '\n':
		# '\n' is a single character
			if count == index:
				end = i
				return start, end
			count += 1
			if count == index:
				start = i + 1
		else:
			print('\n')
	return -1


# ---------------------------------------------------- File Procedures #


  #


# General Procedures ------------------------------------------------- #

def lists_to_tuple(list1, list2):
	# Returns a list of tuples containing the two list's values
	tpl = []
	if len(list1) == len(list2):
		for i in range(0, len(list1)):
			tpl.append((list1[i], list2[i]))
	else:
		return -1
	return tpl

def new_log(log):
	# Appends log, bump, and time to data files
	FM.append_substring('logs', log + '\n')
	FM.append_substring('bumps', '3\n')
	FM.append_substring('dates', current_time() + '\n')

def current_time():
	# Returns current time (month/day/year hour:minute)
	now = datetime.datetime.now()
	return(now.strftime('%m/%d/%Y %H:%M'))

def bump(indx):
	bump = FM.get_substring('bumps', indx)
	bump = int(bump[:-1]) + 1
	FM.edit_substring('bumps', indx, bump)

# ------------------------------------------------- General Procedures #

# Copyright 2017 Neil Graham
