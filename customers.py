from banques import Banks


class Coustomrs :
    def __init__(self , first_name , last_name , age , bank) :
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.bank = bank

    def __str__(self) :
        return self.first_name + self.last_name + self.age + self.bank.name


bank1 = Banks( "ING" )
coustome = Coustomrs( "Evrard" , "sibo" , 40 , bank1 )
print(coustome.bank.name)
