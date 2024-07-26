class House:
    houses_history = []

    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args[0])
        return super().__new__(cls)  # <- добавлено

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __del__(self):
        print(f'{self.name} has been demolished, but it will remain in history')


h1 = House('Lighthouse', 11)
print(House.houses_history)
h2 = House('Barn', 21)
print(House.houses_history)
h3 = House("Empire State Building", 102)
print(House.houses_history)

del h2
del h3

print(House.houses_history)

