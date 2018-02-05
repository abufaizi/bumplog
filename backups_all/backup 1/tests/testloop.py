string = 'Hello goodbye'
for i in range(0, len(string)):
    print(string[i] + '/i:' + str(i) + '/lenstring:' + str(len(string)))
    string = string[1:]
