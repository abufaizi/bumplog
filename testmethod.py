import UI

test_variables = ['general/', 'general/programming/c++/', 'general/business/']

for i in range(0,len(test_variables)):
    print(test_variables[i] + ': ' + UI.get_category(test_variables[i]))
