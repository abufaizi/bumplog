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
        '''
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
        '''
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
