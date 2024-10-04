from person import Person


class Patient(Person):
    def __init__(self,first_name, last_name, age, adress):
        super().__init__(first_name, last_name, age, adress)
    def display_patient(self):
        super().display_person()