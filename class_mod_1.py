class House:

   def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

   def  go_to(self, new_flor):
       flor_ = 0
       if new_flor > self.number_of_floors:
           print('Такого этажа не существует')
       if new_flor <= self.number_of_floors:
           flor_ = new_flor
           for i in range(1, flor_ + 1):
               print(i)
               i+=1


h1 = House('ЖК Горский', 18)

h2 = House('Домик в деревне', 2)

h1.go_to(5)

h2.go_to(10)

