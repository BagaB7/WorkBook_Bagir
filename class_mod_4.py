class House:

    houses_history = []

    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args[0])
        return object.__new__(cls)

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

    def __del__(self):
        print(f'{self.name} снесён, но он останется в истории')

    def __str__(self):
        return f'Название: {self.name} кол-во этажей: {self.number_of_floors}'

    def __len__(self):
            return self.number_of_floors

    def __eq__(self, other):
        if isinstance(other, House):
             return self.number_of_floors == other.number_of_floors
        else:
            return False

    def __ne__(self, other):
        if isinstance(other, House):
            return self.number_of_floors != other.number_of_floors
        else:
            return True

    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors
        else:
            return NotImplemented

    def __le__(self, other):
        if isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors
        else:
            return NotImplemented


    def __gt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors > other.number_of_floors
        else:
            return NotImplemented

    def __ge__(self, other):
        if isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors
        else:
            return NotImplemented

    def __add__(self, value):
        if isinstance(value, int):
            return House(self.name, self.number_of_floors + value)
        if isinstance(value, House):
            return House(self.name, self.number_of_floors + value.number_of_floors)
        else:
            return NotImplemented

    def __radd__(self, value):
        return self.__add__(value)

    def __iadd__(self, value):
        return self.__add__(value)




h1 = House('ЖК Эльбрус', 10)

print(House.houses_history)

h2 = House('ЖК Акация', 20)

print(House.houses_history)

h3 = House('ЖК Матрёшки', 20)

print(House.houses_history)

del h2
del h3

print(House.houses_history)


