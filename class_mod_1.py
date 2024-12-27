class House:

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        flor_ = 0
        if new_floor > self.number_of_floors:
            print(f'Такого этажа не существует. Всего этажей → {self.number_of_floors}')
        if new_floor <= self.number_of_floors:
            flor_ = new_floor
            for i in range(1, flor_ + 1):
                print(f'Этаж → {i}')
                i += 1


h1 = House('ЖК Горский', 18)

h2 = House('Домик в деревне', 2)

h1.go_to(5)

h2.go_to(10)
