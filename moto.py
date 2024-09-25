from vehicule import Vehicle


class Moto(Vehicle):
    tire = 2

    def __init__(self, brand,model,color):
        super().__init__(brand,model,color)
    def accelerate(self):
        print(f"{self.model} Accelerating...")
    def brake(self):
        print(f"{self.model} Braking...")

quad1 = Moto("Honda","Civic","White")
quad1.accelerate()