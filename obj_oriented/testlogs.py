import DM

position = 'general/'

file_paths, log_paths = DM.gather_paths(position)

logs = DM.gather_logs(file_paths, log_paths)

print(logs)


'''import FM

FM.change_directory('data/general/')
FM.edit_substring('notes', 5, 'hello')
'''
