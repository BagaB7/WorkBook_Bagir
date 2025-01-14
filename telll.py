
def custom_write(file_name, strings):
    file_name = 'test.txt'
    file = open(file_name, 'w', encoding='utf-8')
    dict_ = {}
    line_ = 0
    for i in strings:
        line_ += 1
        tell_ = file.tell()
        file.write(f'{i}\n')
        dict_[(line_, tell_)] = i
    file.close()
    return dict_

info = [

    'Text for tell.',

    'Используйте кодировку utf-8.',

    'Because there are 2 languages!',

    'Спасибо!'

    ]



result = custom_write('test.txt', info)

for elem in result.items():

  print(elem)



