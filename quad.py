from vehicule import Vehicle


class Quad(Vehicle):
    tires = 3
    def __init__(self, brand,model,color):
        super().__init__(brand,model,color)
    def accelerate(self):
        print(f"{self.model} Accelerating...")
    def brake(self):
        print(f"{self.model} Braking...")
quad = Quad("BMW","s1000rr","red")
quad.brake()