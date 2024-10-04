from person import Person


class Employ(Person):
    def __init__(self, first_name, last_name, age, adress, salary, poste):
        super().__init__(first_name, last_name, age, adress)

        self.salary = salary
        self.poste = poste
    def display_employ(self):
        super().display_person()
        print(f"Salary : {self.salary} Post : {self.poste}")