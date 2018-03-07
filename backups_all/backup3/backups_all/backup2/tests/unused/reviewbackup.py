
###SECOND REV###

def review(win):
	# Global Variable Declarations
	global logs_all, logs_chsn, bumps_all, log_typd

	# All Logs
	logs_all = setup_logs()
	# Chosen Logs
	logs_chsn = []
	# All Bumps
	bumps_all = total_bumps(logs_all)
	# Typed Log
	log_typd = ''
	# Highlighted Log
	log_highlight = -1

	# Global Variables inside While Loop
	global y_left
	while True:
		# Terminal Width and Height
		x, y = UI.terminal_dimensions()
		x, y = int(x), int(y)
		# Print Width and Margin
		p_wdth, p_mrgn = hor_info(x, 52)

		# Full Height of terminal
		y_left = y
		# Height of header, divider, divider margin, and bottom margin
		h_header, h_divider, h_dividermrgn, h_bottommrgn = 3, 1, 1, 2
		y_left = y_left - h_header - h_divider - h_dividermrgn - h_bottommrgn
		# Height of Typed Log
		y_left -= section_height(log_typd, p_wdth)

		# Spacing Between each log
		spacing_btwn = 2
		# Height of Chosen Logs
		log_end, y_left = check_chsn(y_left, p_wdth, spacing_btwn)

		# If log_end was not set...
		if log_end == -1:
			# ... not enough logs are chosen, therefore choose more logs
			log_end, y_left = choose_logs(y_left, p_wdth, spacing_btwn)

		# Clear and print each part of the terminal screen
		print_screen(win, x, log_end, p_wdth, p_mrgn, spacing_btwn)

		# Only returns if it gets some form of keyboard input
		key = get_input(win)
		if key == 'KEY_RESIZE':
			continue
		elif str(key) == '\\':
			typed = typed[:-1]
			continue
		elif key == '\n':
			typed = ''
			continue
		elif key == 'KEY_UP':
			continue
		elif key == 'KEY_DOWN':
			continue
		typed += str(key)



def check_chsn(y_left, p_wdth, spacing):
#Global Variables: logs_chsn
	# Height of each log in Chosen Logs and Spacing inbetween
	log_end = -1
	for i in range(0, len(logs_chsn)):
		log = FM.get_substring('logs', logs_chsn[i])
		y_aftr = y_left - spacing - section_height(log, p_wdth)
		if y_aftr < 0:
			log_end = i
			break
		else:
			y_left = y_aftr
	return log_end, y_left

def choose_logs(y_left, p_wdth, spacing):
#Global Variables: logs_all, logs_chsn, bumps_all
	while True:
		indx = random_log(logs_all, bumps_all)
		log_item = logs_all.pop(indx)
		logs_chsn.append(log_item[0])
		bumps_all -= log_item[1]
		log = FM.get_substring('logs', logs_chsn[-1])
		y_aftr = y_left - spacing - section_height(log, p_wdth)
		if y_aftr < 0:
			log_end = len(logs_chsn)
			break
		else:
			y_left = y_aftr
	return log_end, y_left

def print_screen(win, x, log_end, p_wdth, p_mrgn, spacing_btwn):
#Global Variables: logs_all, logs_chsn, log_typd, y_left
	UI.clear_screen(win)
	UI.print_header(win, p_wdth, x)
	for i in range(0, int(y_left/2)):
		UI.new_line(win)
		y_left -= 1
	for i in range(0, log_end):
		log = FM.get_substring('logs', logs_chsn[i])
		UI.print_section(win, log, p_wdth, p_mrgn)
		for c in range(0, spacing_btwn + 1):
			UI.new_line(win)
	for i in range(0, y_left + 1):
		UI.new_line(win)
	UI.print_divider(win, x)
	UI.print_section(win, log_typd, p_wdth, p_mrgn)

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


###FIRST REV###

def review(win, content):
	# Keep track of all logs shown and show logs w/ respect to bumps,
	# given list of all (logs, bumps, dates)
	logs = setup_logs()
	all_bumps = total_bumps(logs)
	logs_chosen = []
	typed = ''
	while True:
		inf = {}
		key = ''
		log_end = 0
		x, y = UI.terminal_dimensions()
		x, y = int(x), int(y)
		width, margin = hor_info(x, 52)
		y_left = y - 7
		inf['y_left 1'] = y_left
		complete = False
		y_left = y_left - 1 - section_height(typed, width)
		#y_left, log_end = check_chosen(logs_chosen, )
		for i in range(0, len(logs_chosen)):
			y_new = y_left - 1 - section_height(FM.get_substring('logs', logs_chosen[i]), width)
			if y_new < 0:
				log_end = i
				complete = True
				break
			elif y_new == 0 and len(logs_chosen) > i:
				log_end = i+1
				complete = True
				break
			else:
				y_left = y_new
		inf['y_left 2'] = y_left
		if not complete:
			while True:
				rand_num = random_log(logs, all_bumps)
				log_item = logs.pop(rand_num)
				all_bumps -= log_item[1]
				logs_chosen.append(log_item[0])
				y_new = y_left - 1 - section_height(FM.get_substring('logs', log_item[0]), width)
				if y_new < 0:
					log_end = len(logs_chosen)
					break
				else:
					y_left = y_new
		inf['y3'] = y_left
		UI.clear_screen(win)
		#UI.print_info(win, x, inf)
		UI.print_header(win, x, info.category(), info.name())
		# for i in range(0, int(y_left/2)):
		# 	# Print Upper Margins
		# 	y_left -= 1
		# 	UI.new_line(win)
		for i in range(0, log_end):
			# Print All Logs
			log = FM.get_substring('logs', logs_chosen[i])
			UI.print_section(win, log, width, margin)
			UI.new_line(win)
			UI.new_line(win)
		# for i in range(0, y_left):
		# 	# Print Lower Margins
		# 	y_left -= 1
		# 	UI.new_line(win)
		UI.print_footer(win, x)
		UI.print_section(win, typed, width, margin)
		while True:
			try:
				key = win.getkey()
				if key == os.linesep:
					break
			except Exception as e:
				pass
			if key != '':
				break
		if key == 'KEY_RESIZE':
			continue
		elif str(key) == '\\':
			typed = typed[:-1]
			continue
		elif key == '\n':
			typed = ''
			continue
		elif key == 'KEY_UP':
			continue
		typed += str(key)
