
# Review Module
#   Reviews Logs of Information Non-Linearly


# Local Modules
import FM
import UI
import LP

# NonLocal Modules
import math


def main(win):
	# All Logs
	logs_all = LP.indx_and_bump()
	# Chosen Logs
	logs_chsn = []
	# All Bumps
	bumps_all = LP.total_bumps(logs_all)
	# Typed Log
	log_typd = ''

	first_run = True
	# Highlighted Log
	highlight = -1
	while True:

		# Terminal Width and Height
		x, y = UI.terminal_dimensions()
		x, y = int(x), int(y)
		# Print Width and Margin
		p_wdth, p_mrgn = LP.hor_info(x, 52)

		# Full Height of terminal
		y_left = y
		# Height of header, divider, divider margin, and bottom margin
		h_header, h_divider, h_dividermrgn, h_bottommrgn = 3, 1, 1, 2
		y_left = y_left - h_header - h_divider - h_dividermrgn - h_bottommrgn
		# Height of Typed Log
		y_left -= LP.section_height(log_typd, p_wdth)

		# Spacing Between each log
		spacing_btwn = 1
		# Height of Chosen Logs
		log_end, y_left = check_chsn(logs_chsn, y_left, p_wdth, spacing_btwn)

		# If log_end was not set...
		if log_end == -1:
			# ... not enough logs are chosen, therefore choose more logs
			logs_all, logs_chsn, bumps_all, log_end, y_left = choose_logs(
			logs_all, logs_chsn, bumps_all, y_left, p_wdth, spacing_btwn)

		# If this is the first run, go through again
		if first_run:
			first_run = False
			continue

		# If highlight is out of range, set it back to nothing
		if highlight >= log_end:
			highlight = -1

		# Clear and print each part of the terminal screen
		print_screen(win, logs_chsn, log_end, log_typd, p_wdth, p_mrgn,
		x, y_left, spacing_btwn, highlight)

		# Only returns if it gets some form of keyboard input
		key = get_input(win)
		if key == 'KEY_RESIZE':
			continue
		elif key == 'KEY_UP':
			if highlight == -1:
				highlight = log_end - 1
			else:
				highlight -= 1
			continue
		elif key == 'KEY_DOWN':
			if highlight == log_end - 1:
				highlight = -1
			else:
				highlight += 1
			continue
		elif key == 'KEY_RIGHT' or key == 'KEY_LEFT':
			if highlight >= -1:
				logs_chsn = logs_chsn[log_end:]
				first_run = True
				continue
		elif key == 'KEY_BACKSPACE' or ord(key) == 127:
			log_typd = log_typd[:-1]
			continue
		elif ord(key) == 27:
			exit()
		elif ord(key) == 10:
			if highlight > -1:
				LP.bump(logs_chsn[highlight])
			else:
				if len(log_typd) > -1:
					LP.new_log(log_typd)
					log_typd = ''
			continue
		log_typd += str(key)


def print_screen(win, logs_chsn, log_end, log_typd, p_wdth, p_mrgn,
x, y_left, spacing_btwn, highlight):
	UI.clear_screen(win)
	UI.print_header(win, p_wdth, x)
	for i in range(0, int(y_left/2)):
		UI.new_line(win)
		y_left -= 1
	for i in range(0, log_end):
		log = FM.get_substring('logs', logs_chsn[i])
		if i == highlight:
			UI.highlight_center(win, log, p_wdth, x, True)
		else:
			UI.print_center(win, log, p_wdth, x, True)
		for c in range(0, spacing_btwn):
			UI.new_line(win)
	for i in range(0, y_left):
		UI.new_line(win)
	UI.print_divider(win, x)
	UI.print_left(win, log_typd, p_wdth, p_mrgn)


def check_chsn(logs_chsn, y_left, p_wdth, spacing):
	# Height of each log in Chosen Logs and Spacing inbetween
	log_end = -1
	for i in range(0, len(logs_chsn)):
		log = FM.get_substring('logs', logs_chsn[i])
		y_aftr = y_left - spacing - LP.section_height(log, p_wdth)
		if y_aftr < 0:
			log_end = i
			break
		else:
			y_left = y_aftr
	return log_end, y_left

def choose_logs(logs_all, logs_chsn, bumps_all, y_left, p_wdth, spacing):
	while True:
		# if len(logs_all) == 0:
		# 	log_end = len(logs_chsn + 1)
		# 	break
		indx = LP.bump_index(logs_all, bumps_all)
		log_item = logs_all.pop(indx)
		logs_chsn.append(log_item[0])
		bumps_all -= log_item[1]
		log = FM.get_substring('logs', logs_chsn[-1])
		y_aftr = y_left - spacing - LP.section_height(log, p_wdth)
		if y_aftr < 0:
			log_end = len(logs_chsn)
			break
		else:
			y_left = y_aftr
	return logs_all, logs_chsn, bumps_all, log_end, y_left

def get_input(win):
	key = ''
	while True:
		try:
			key = win.getkey()
			if key == os.linesep:
				break
		except Exception as e:
			pass
		if key != '':
			return key


# Copyright 2017 Neil Graham
