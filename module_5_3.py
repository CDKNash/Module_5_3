class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __eq__(self, other):
        return self.number_of_floors == other.number_of_floors

    def __add__(self, value):
        if isinstance(value, int):
            return self.number_of_floors + value

    def __iadd__(self, value):
        if isinstance(value, int):
            return self.number_of_floors + value

    def __radd__(self, value):
        if isinstance(value, int):
            return self.number_of_floors + value


    def __lt__(self, other):
        return self.number_of_floors < other.number_of_floors
    def __le__(self, other):
        return self.number_of_floors <= other.number_of_floors
    def __gt__(self, other):
        return self.number_of_floors > other.number_of_floors
    def __ge__(self, other):
        return self.number_of_floors >= other.number_of_floors
    def __ne__(self, other):
        return self.number_of_floors != other.number_of_floors




house1 = House('ЖК Изумрудный', 18)
house2 = House('Поселок ЦДК', 2)

print('Название:', house1.name+', ', 'кол-во этажей:', house1.number_of_floors)
print('Название:', house2.name+', ', 'кол-во этажей:', house2.number_of_floors)

print(house1 == house2) # __eq__

house2.number_of_floors = house2.number_of_floors + 16 # __add__
print('Название:', house2.name+', ', 'кол-во этажей:', house2.number_of_floors)
print(house1 == house2)

house1.number_of_floors += 12 # __iadd__
print('Название:', house1.name+', ', 'кол-во этажей:', house1.number_of_floors)

house2.number_of_floors = 12 + house2.number_of_floors # __radd__
print('Название:', house2.name+', ', 'кол-во этажей:', house2.number_of_floors)

print(house1 < house2)  # __gt__
print(house1 <= house2) # __ge__
print(house1 > house2) # __lt__
print(house1 >= house2)  # __le__
print(house1 != house2) # __ne__