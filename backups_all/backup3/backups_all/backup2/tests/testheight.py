import LP
import UI

x, y = UI.terminal_dimensions()
x, y = int(x), int(y)

width, margin = LP.ui_width(x)

logs = ['', 'hello goodbye', 'jlk dsaflkja sdlkfj alskdfj lkasdj fklajsd flkja sdfklj asdlfkj asdlkfj alskdjf laksdjf lkajdsf lkjad slfkas']
for log in logs:
    print('\'' + log + '\': ' + str(LP.log_height(log, width)))
