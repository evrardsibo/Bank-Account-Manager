class Vehicle:
    tire = 0
    def __init__(self, brand, model,color):
        self.brand = brand
        self.model = model
        self.color = color

    def accelerate(self):
        print(f"{self.brand} {self.model} {self.color} Accelerating...")

    def reculer(self):
        print(f"{self.brand} {self.model} {self.color} Reculerating...")

car = Vehicle('BMW','X5','White')
car1 = Vehicle("Opel","Astra","Black")
car.accelerate()
car1.reculer()