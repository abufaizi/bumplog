
# Data Management
#    Reads and writes data to the data folder

import procedures.FM

# Gather data paths at position
def gather_paths(position):
    # cd to position and gather log paths and strengths
    FM.change_directory('data/' + position)
    paths = FM.get_all('notes')

    # separate paths information by comma and put into list
    for i in range(0,len(paths)):
        paths[i] = paths[i].split(',')
        for n in range(0, len(paths[i])):
            paths[i][n] = int(paths[i][n])

    # find number of layers position is from data folder
    layers = 0
    for i in range(0,len(position)):
        if position[i] == '/':
            layers += 1

    # cd back to logs folder (could be any of the ordered data folders)
    FM.change_directory('../' * layers + 'ordered/logs/')
    # get all file names in logs folder
    file_names = FM.list_files()

    # find number in each file name (take out .txt and convert to int)
    for i in range(0,len(file_names)):
        for n in range(0,len(file_names[i])):
            if file_names[i][n] == '.':
                file_names[i] = int(file_names[i][:n])
                break

    # file_paths is for knowing the filename for the first
    file_paths = []
    log_paths = []

    # store each necessary file name in file_paths
    for i in range(0,len(file_names)):
        for n in range(0,len(paths)):
            if paths[n][0] == file_names[i]:
                file_paths.append(file_names[i])
                break

    # setup log_paths for each file in file_paths
    for i in range(0,len(file_paths)):
        log_paths.append([])

    # organize log and strength with their respective file
    for i in range(0,len(file_paths)):
        for n in range(0,len(paths)):
            if paths[n][0] == file_paths[i]:
                log_paths[i].append([paths[n][1], paths[n][2]])

    # cd back to bumplog folder
    FM.change_directory('../../../')

    return file_paths, log_paths


# Gather logs from ordered data
def gather_logs(file_paths, log_paths):
    # cd to logs folder
    FM.change_directory('data/ordered/logs/')

    logs = []

    for i in range(0,len(file_paths)):
        gathered_data = FM.get_all(str(file_paths[i]))
        print('Len(gathered_data): ' + str(len(gathered_data)))
        for n in range(0,len(log_paths[i])):
            path = log_paths[i][n][0]
            log = gathered_data[path]
            strn = log_paths[i][n][1]
            logs.append([log,strn])

    FM.change_directory('../../../')

    return logs
