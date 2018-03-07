'''
import UI

test_variables = ['general/', 'general/programming/c++/', 'general/business/']

for i in range(0,len(test_variables)):
    print(test_variables[i] + ': ' + UI.get_category(test_variables[i]))
'''

'''
import DM

file_paths, log_paths = DM.gather_paths('general/')

print('file_paths:')
print(file_paths)
print()
print('log_paths:')
print(log_paths)
print()
logs = DM.gather_logs(file_paths, log_paths)
print('logs:')
print(logs)
print()
print('logs[0]')
print(logs[0])
'''

import FM

FM.change_directory('data/ordered/logs/')
print(FM.get_all('3'))
