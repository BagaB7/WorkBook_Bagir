immutable_var = 1,2,3, 'one'
print(immutable_var)
# print(immutable_var  .replace('1','2')) # тип данных класса tuple/кортеж  не изменяемая
test = '1,2,3'
# print(test .replace('1','2')) # так же код с типом int уже работает
mutable_list = ([1, 2, 3, 'one'])
#mutable_list [0] = 'one'
#mutable_list [3] = 1
#mutable_list [2] = 2
#mutable_list [1] = 3
print(mutable_list[::-1]) # Аахаха  мучался мучался, вспомнил про [::-1]








