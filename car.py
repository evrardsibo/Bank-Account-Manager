from vehicule import Vehicle


class Car(Vehicle):
    tires = 4
    def __init__(self, brand,model,color):
        super().__init__(brand,model,color)
    def accelerate(self):
        print(f"{self.model} Accelerating...")
    def brake(self):
        print(f"{self.model} Braking...")

