def upper(text: str) -> str:
    text = text.upper()
    return text


test = upper('hello')
print(test)


class Vehicle:
    def __init__(self, fuel):
        self.fuels: int = fuel

    def printout(self):
        print(self.fuels)


car = Vehicle(100)
car1 = Vehicle(200)

car.fuel = 'sa'
car1.fuel = 'sa'

car.printout()
car1.printout()
