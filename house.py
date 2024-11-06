class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to (self, new_floor):
        if 1 <= new_floor <= self.number_of_floors:
            print(f'Вы переехали на {new_floor} этаж, в доме {self.name}')
        else:
            print('Такого этажа не существует')


h1 = House('ЖК Весенний', 18)

h2 = House('ЖК СНТ-АГРО', 2)

h1.go_to(8)

h2.go_to(5)









