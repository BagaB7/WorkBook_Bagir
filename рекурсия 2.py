def calculate_structure_sum(args):
    sum_ = 0

    if isinstance(args, (list, tuple, set)):
        for i in args:
            sum_ += calculate_structure_sum(i)

    if isinstance(args, dict):
        for key, value in args.items():
            sum_ += calculate_structure_sum(key)
            sum_ += calculate_structure_sum(value)

    if isinstance(args, (int, float)):
        sum_ += args

    if isinstance(args, str):
        sum_ += len(args)
    return sum_

data_structure = [

  [1, 2, 3],
  {'a': 4, 'b': 5},

  (6, {'cube': 7, 'drum': 8}),

  "Hello",

  ((), [{(2, 'Urban', ('Urban2', 35))}])

]
print(calculate_structure_sum(data_structure))
