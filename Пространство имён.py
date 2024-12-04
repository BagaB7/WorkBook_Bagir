calls = 0           # переменная вне функции

def coutn_calls():
    global calls    # используем переменную из вне фукнции
    calls += 1      # добавляем + 1

def string_info(string):
    coutn_calls()   # используем 1-ю функцию для подсчета
    return (len(string), string.upper(), string.lower())  # проходим по всей длине аргумента и меняем регистры

def is_contains(string, list_to_search):
    coutn_calls()
    return string.lower() in [item.lower() for item in list_to_search]
    #  это генератор списка, который преобразует каждый элемент
    #  item из списка list_to_search в нижний регистр и создает новый список.


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)


