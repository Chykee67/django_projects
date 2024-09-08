class Car:
    now = 4
    def __init__(self, maker:str, yop:int, price:str, mileage:str):
        self.maker = maker
        self.yop = yop
        self.price = price
        self.mileage = mileage

    def __str__(self):
        return self.model

class Benz(Car):
    salary = 700000
    qty = 7

    def __init__(self, maker, model:str, yop, price, mileage):
        super().__init__(maker, yop, price, mileage)
        self.model = model

    def deal(self):
        return self.salary/self.qty

class Garage(Benz):
    owner:str = 'chikeluba'

    def __str__(self):
        return self.owner

garage = Garage('mercedes', 'c350', 2022, 'two million', 'three kilometers')

garage.salary = 7000

print(garage.deal())