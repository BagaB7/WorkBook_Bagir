my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
quantity = len(my_list)   
i = 0                     
while i < (quantity):      
    if my_list[i] == 0:    
     i = i + 1             
     continue             
    if my_list[i] > 0:     
        print(my_list[i])
        i = i +1
    elif my_list[i] < 0:
        break


















# while 1>0  команда вайл будет повторять цикл т.к 1 всегда больше нуля
# continue  т.к цикл будет повторяться и до строк ниже не дойдет, это команда запустит строки ниже и вернется к циклу
# break если условия не выполнено, то цикл остановится
