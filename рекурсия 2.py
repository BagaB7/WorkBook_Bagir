def calculate_structure_sum(arg):
    sum_ = 0

    if isinstance(arg, (list, tuple, set)):
        for i in arg:
            sum_ += calculate_structure_sum(i)

    if isinstance(arg, dict):
        for key, value in arg.items():
            sum_ += calculate_structure_sum(key)
            sum_ += calculate_structure_sum(value)

    if isinstance(arg, (int, float)):
        sum_ += arg

    if isinstance(arg, str):
        sum_ += len(arg)
    return sum_

data_structure = [

  [1, 2, 3],
  {'a': 4, 'b': 5},

  (6, {'cube': 7, 'drum': 8}),

  "Hello",

  ((), [{(2, 'Urban', ('Urban2', 35))}])

]
print(calculate_structure_sum(data_structure))