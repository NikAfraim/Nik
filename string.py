def upper(text: str) -> str:
    text = text.upper()
    return text


test = upper('hello')
print(test)


class Vehicle:
    fuel: int = 'sds'

    def printout(self):
        print(self.fuel)


car = Vehicle()
car1 = Vehicle()
Vehicle.fuel = 'hx'
car.fuel = 300
Vehicle.printout(car)
Vehicle.printout(car1)
