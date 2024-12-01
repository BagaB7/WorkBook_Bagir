def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append(value)
    print(matrix)
    return matrix
n = int(input('Кличество строк: '))
m = int(input('Кличество столбцов: '))
value = int(input('Значение матрицы: '))
matrix = get_matrix(n, m, value)
print()
if n <= 0 or m <= 0:
    print("\033[34m" '!!!Количество строк или столбцов указано неверно!!!') # пока не смог красный сделать :X
