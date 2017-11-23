
# Keyboard Input
#   For real-time keyboard input


# NonLocal Modules
#from pynput import keyboard

'''
import curses

def mainy(win):
    recorded = ''
    win.nodelay(True)
    key=""
    win.clear()
    win.addstr("Detected key:")
    while 1:
        try:
            key = win.getkey()
            if str(key) == 'KEY_UP':
                recorded = recorded[:-1]
            else:
                recorded += str(key)
            win.clear()
            win.addstr("Detected key:")
            win.addstr(str(key))
            win.addstr('\n')
            win.addstr(recorded)
            if key == os.linesep:
                break
        except Exception as e:
           # No input
           pass

def main(win):
    win.nodelay(True)
    key=""
    win.clear()
    win.addstr("Detected key:")
    while 1:
        try:
            key = win.getkey()
    #         if str(key) == 'KEY_UP':
    #             recorded = recorded[:-1]
    #         else:
    #             recorded += str(key)
    #         win.clear()
    #         win.addstr("Detected key:")
    #         win.addstr(str(key))
    #         win.addstr('\n')
    #         win.addstr(recorded)
    #         if key == os.linesep:
    #             break
        except Exception as e:
           # No input
           pass

curses.wrapper(main)





import curses

def main(win):
	key = ''
	win.nodelay(True)
	win.clear()
	win.addstr('test1')
	test2(win, 'ayyyy')
	while 1:
		try:
			key = win.getkey()
		except Exception as e:
			pass

	#test2(arg1)

def test2(win, arg1):
	win.addstr('test2')
	win.addstr(arg1)
'''
