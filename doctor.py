from employ import Employ


class Doctor(Employ):
    def __init__(self ,first_name, last_name, age, adress, salary, poste,specialisation):
        super().__init__(first_name, last_name, age, adress, salary, poste)
        self.specialisation = specialisation

    def dispay_doctor(self):
        super().display_employ()
        print(f"Specialasation : {self.specialisation}")
