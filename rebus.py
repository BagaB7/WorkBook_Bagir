def  get_passord(number):
    pass_ = ''
    for i in range(1, number):
        for j in range(2, number):
            if j <= i:
                continue
            if number % (i + j) == 0:
                pass_ += str(i) + str(j)
    return pass_
while True:
    pass_a = int(input('Введите число от 3 до 20: '))
    result = get_passord(pass_a)
    print('Пароль',result)




