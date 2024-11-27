fistr = int(input('Введите первое число: '))
second = int(input('Введите второе число: '))
third = int(input('Введите третье число: '))
if fistr == second == third:
    print('3')
elif fistr == second or fistr == third or second == third:
    print('2')
else:
    print('0')