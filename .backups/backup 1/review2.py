
# Rereview Module
#   R

import FM
import UI
import LP

# NonLocal Modules
import math
import datetime

def main():
    # Class implementation

    # REMOVES logs_all, bumps_all

    # USES logs_chsn, log_typd, first_run, highlight
    # ADDS log_paths, file_paths, logs, strn

    nclass = 'general'
    name = 'Neil Graham'

    log_paths, file_paths = parse_class(nclass)

    logs = []
    strn = []

    for i in range(0,len(file_paths)):
        for n in range(0,len(log_paths[i])):
            file_name = str(file_paths[i])
            log_index = log_paths[i][n]
            logs.append(FM.get_substring(file_name, log_index[0]))
            strn.append(bump_strength(log_index[1]))

    #Test

    for i in range(0, len(logs)):
        print('\"' + logs[i] + '\"    ' + str(strn[i]))

    #Test

'''
    logs_chsn = []

    log_typd = ''

    first_run = True

    highlight = -1

    while True:

        x, y = UI.terminal_dimensions()
        x, y = int(x), int(y)

        p_wdth, p_mrgn = LP.hor_info(x, 52)


        y_left = y

        h_header, h_divider, h_dividermrgn, h_bottommrgn = 3, 1, 1, 2
        y_left = y_left - h_header - h_divider - h_dividermrgn - h_bottommrgn

        y_left -= LP.section_height(log_typd, p_wdth)


        spacing_btwn = 1

        log_end, y_left = check_chsn(logs_chsn, y_left, p_wdth, spacing_btwn)


        if log_end == -1:
            # CONTAINS logs_all
            logs_all, logs_chsn, bumps_all, log_end, y_left = choose_logs(
            logs_all, logs_chsn, bumps_all,
            )

'''


'''
# WIP
def release(release_dates):
    #The list of release dates will be in chronological order. [['1/2/18 12:00', 1, 8], ]

    #If the release year is the year before the current year, then
    # skip all next steps and release the note

    now = datetime.datetime.now()
'''

#    now_date = now.strftime('%m/%d/%Y %H:%M')
'''
    now_date = parse_date(now_date)
    released = []
    for i in range(0,len(release_dates)):
        log_date = parse_date(release_dates[i][0])
        passes = True
        for n in range(0,3):
            if log_date[-3-n] == now_date[-3-n]:
                continue
            elif log_date[-3-n] < now_date[-3-n]:
                break
            else:
                passes = False
                break
        if passes:
            for n in range(0,2):
                if log_date[3+n] == now_date[3+n]:
                    continue
                elif log_date[3+n] < now_date[3+n]:
                    break
                else:
                    passes = False
                    break
        if passes:
            if i == len(release_dates) - 1:
                released.append( release_dates[i][1:] )
                return released, []
            else:
                released.append( release_dates[i][1:] )
        else:
            for n in range(0,len()):
            return released, release_dates( len(released) - 1 : )
'''




def parse_date(str_date):
    date = str_date.split()
    day = date[0].split('/')
    time = date[1].split(':')
    date = []
    for i in range(0,3):
        date.append(int(day[i]))
    for i in range(0,2):
        date.append(int(time[i])
    return date







def parse_class(nclass):
    # cd to classes folder and parse /class info
    FM.change_directory('classes')
    info = FM.get_all(nclass)

    # split each cl ass info into a list of 3, (file_num, log_num, bump_cnt)
    for i in range(0,len(info)):
        info[i] = info[i].split(',')
        for n in range(0,len(info[i])):
            info[i][n] = int(info[i][n])

    # cd to logs folder
    FM.change_directory('../logs')
    # get all file names in logs folder
    file_names = FM.list_files()

    # find number in file name by ending string where '.' is
    for i in range(0,len(file_names)):
        for n in range(0,len(file_names[i])):
            if file_names[i][n] == '.':
                file_names[i] = int(file_names[i][:n])
                break

    log_paths = []
    file_paths = []

    for i in range(0,len(file_names)):
        for n in range(0,len(info)):
            if info[n][0] == file_names[i]:
                file_paths.append(file_names[i])
                break

    for i in range(0,len(file_paths)):
        log_paths.append([])

    for i in range(0,len(file_paths)):
        for n in range(0,len(info)):
            if info[n][0] == file_paths[i]:
                log_paths[i].append([info[n][1],info[n][2]])

    return log_paths, file_paths


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

        #CONTAINS logs_all

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


def bump_strength(bump):
	#For attributing a incrementally decreasing strength to bumps
	return (10*bump)**(1/2)+1


main()


# Copyright 2017 Neil Graham
