my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
quantity = len(my_list)    # вывели число строки
i = 0                      # добавили 0 в переменую
while i < (quantity):      # создали цикл который будет повторяться пока переменная лен больше нуля
    if my_list[i] == 0:    # создаем условие где если 0 равен нулю
     i = i + 1             # добавляем + 1
     continue              # условия цикла если выполнится, цикл не повторится с 1 строки а будет читаться дальше
    if my_list[i] > 0:     # условие где 
        print(my_list[i])
        i = i +1
    elif my_list[i] < 0:
        break


















# while 1>0  команда вайл будет повторять цикл т.к 1 всегда больше нуля
# continue  т.к цикл будет повторяться и до строк ниже не дойдет, это команда запустит строки ниже и вернется к циклу
# break если условия не выполнено, то цикл остановится
