def print_params(a = 1, b = 'string', c = 'True'):
    print(a, b ,c)

print_params()
print_params(b = 25)
print_params(c = [1,2,3])

values_list = ['Urban', '777', [6,9,'ban']]
values_dict = {'a': 1, 'b': 2, 'c': 3}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [2 , 3]

print_params(*values_list_2)