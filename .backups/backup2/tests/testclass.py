
# For

import FM

# Change directory to classes folder
FM.change_directory('classes')
# Get all
logs = FM.get_all('general')

# Parses list of (file_index, log_index, log_bump) from class file
for i in range(0,len(logs)):
    logs[i] = logs[i].split(',')
    for n in range(0,len(logs[i])):
        logs[i][n] = int(logs[i][n])

# Change directory to logs folder
FM.change_directory('../logs')
# Get all file names from logs folder
file_indices = FM.list_files()

# Parse all file index numbers from all file names in logs folder
for i in range(0,len(file_indices)):
    for n in range(0,len(file_indices[i])):
        if file_indices[i][n] == '.':
            file_indices[i] = int(file_indices[i][:n])
            break

log_paths = []
file_paths = []

# NEED TO: Create a way to remove file indices that are not
# included in class

for i in range(0,len(file_indices)):
    for n in range(0, len(logs)):
        if logs[n][0] == file_indices[i]:
            file_paths.append(file_indices[i])
            break

# WIP: Create number of lists equal to the number of files
# needed to be accessed
for i in range(0,len(file_paths)):
    log_paths.append([])

# WIP: Partition log data to log_paths
for i in range(0,len(file_paths)):
    for n in range(0,len(logs)):
        if logs[n][0] == file_paths[i]:
            log_paths[i].append([logs[n][1],logs[n][2]])

for i in range(0,len(file_paths)):
    for n in range(0,len(log_paths[i])):
        print(FM.get_substring(str(file_paths[i]), log_paths[i][n][0]))
        print()
