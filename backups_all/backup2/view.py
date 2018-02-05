'''
for i in range(0,len(file_paths)):
	gathered_data = FM.get_all(str(file_paths[i]))
	for n in range(0,len(log_paths[i])):
		print('logs_strn:')
		print(logs_strn)
		path = log_paths[i][n][0]
		print('path: ' + str(path))
		log = gathered_data[path]
		strn = log_paths[i][n][1]
		logs_strn.append([log,strn])
'''

# position and scope can be changed in the semantic tree.
#     Scope is the volume of the sphere,
#     Position is the placement in the parent sphere.

# Each log can be seen as a sphere.
#     The surface of the sphere is the log itself and the
#     volume inside of it are any sublogs to that log.
#
# You could think of the surface of the sphere being created
#  with respect to the position, and the logs inside of that
#  sphere as remaining gaseous until chosen. Chosen logs would
#  materialize from the gaseous material.

# To inform the individual more so about themselves is what
#  we are trying to do

# [+] and [-] at the beginning of each note will change the
#  strength of that note, and will be placed to the left of
#  the log's first
#
# [command / control] and [+]   changes scope
# [command / control] and [-]  changes
#
#In order to change position and scope

# Parsing words and phrases from each and every log in
#  a category.
#
# Relating logs with respect to their similar words and
#  key phrases. Uncommon key phrases build a stronger relation
#  than common words, for example.

# Your program can parse through information when it is
#  not running the user interface.

# goose geese

# In order to strengthen logs on your own, you would select
#  the entire log and press command/control enter. This
#  strengthens everything inside of the selected
#  position and scope

# Set the time in which a log will be seen next. This will be
#  represented by a gradient time scale. The gradient represents
#  the chance of that log occurring in the review of the position
#  and scope

# Do not
