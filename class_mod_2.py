class House:

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
        self.__str__()

    def go_to(self, new_floor):
        flor_ = 0
        if new_floor > self.number_of_floors:
            print(f'Объект - {self.name} такого этажа {new_floor} не существует, всего этажей → {self.number_of_floors}')
        if new_floor <= self.number_of_floors:
            flor_ = new_floor
            for i in range(1, flor_ + 1):
                print(f'Этаж → {i}')
                i += 1
    def __str__(self):
        return f'Название: {self.name} кол-во этажей: {self.number_of_floors}'

    def __len__(self):
        return self.number_of_floors


h1 = House('ЖК Эльбрус', 10)

h2 = House('ЖК Акация', 20)

print(h1)

print(h2)

print(len(h1))

print(len(h2))


