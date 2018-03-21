
# Review Module
#   Reviews Logs of Information Non-Linearly


# Local Modules
import FM
import UI
import LP
import DM

# NonLocal Modules
import math



def main(win):
	# Initial log position and name of user
	position = 'general/'
	name = 'Neil Graham'

	# Gather all logs and bumps with respect to position
	file_paths, log_paths = DM.gather_paths(position)
	logs_all = DM.gather_logs(file_paths, log_paths)

	# Chosen Logs
	logs_chsn = []
	# Weight of all positional logs
	weight_all = LP.total_weight(logs_all)
	# Alert Log
	log_alrt = ''
	# Typed Log
	log_typd = ''
	# Highlighted Log (-1 means no log highlighted)
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
		##h_header, h_divider, h_dividermrgn, h_bottommrgn = 3, 1, 1, 2
		h_header, h_divider, h_dividermrgn, h_bottommrgn = 2, 1, 1, 3
		y_left = y_left - h_header - h_divider - h_dividermrgn - h_bottommrgn
		# Height of Alert Log
		if len(log_alrt) > 0:
			y_left -= len(UI.split_lines(log_alrt, p_wdth)) + 1
		# Height of Typed Log
		y_left -= len(UI.split_lines(log_typd, p_wdth))

		# Spacing Between each log
		spacing_btwn = 2
		# Height of Chosen Logs
		log_end, y_left = check_chsn(logs_chsn, y_left, p_wdth, spacing_btwn)

		# If log_end was not set...
		if log_end == -1:
			# ... not enough logs are chosen, therefore choose more logs
			logs_all, logs_chsn, weight_all, log_end, y_left = choose_logs(
			logs_all, logs_chsn, weight_all, y_left, p_wdth, spacing_btwn)

		# If this is the first run, go through again
		''' MAY NOT BE NECESSARY
		if first_run:
			first_run = False
			continue
		'''

		# If highlight is out of range, set it back to nothing
		if highlight >= log_end:
			highlight = -1

		# Clear and print each part of the terminal screen
		UI.print_screen(win, logs_chsn, log_end, log_typd, log_alrt, p_wdth,
		p_mrgn, x, y_left, spacing_btwn, highlight, position, name)

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

# Height of each item in logs_chsn (as well as spacing_btwn each log)
def check_chsn(logs_chsn, y_left, p_wdth, spacing):
	log_end = -1
	for i in range(0, len(logs_chsn)):
		y_aftr = y_left - spacing - len(UI.split_lines(logs_chsn[i], p_wdth))
		if y_aftr < 0:
			log_end = i
			break
		else:
			y_left = y_aftr
	return log_end, y_left

def choose_logs(logs_all, logs_chsn, weight_all, y_left, p_wdth, spacing):
	while True:
		if len(logs_all) == 0:
			log_end = len(logs_chsn)
			break
		indx = LP.choosewrt_weight(logs_all, weight_all)
		logs_chsn.append(logs_all[indx][0])
		weight_all -= logs_all[indx][1]
		del(logs_all[indx])
		y_aftr = y_left - spacing - len(UI.split_lines(logs_chsn[-1], p_wdth))
		if y_aftr < 0:
			#log_end = len(logs_chsn)
			log_end = len(logs_chsn) - 1
			break
		else:
			y_left = y_aftr
	return logs_all, logs_chsn, weight_all, log_end, y_left


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
