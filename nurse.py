from employ import Employ


class Nurse(Employ):
    def __init__(self,first_name, last_name, age, adress, salary, poste,assignation):
        super().__init__(first_name, last_name, age, adress, salary, poste)
        self.assignation = assignation
    def display_nurse(self):
        super().display_employ()
        print(f"Assignation : {self.assignation}")