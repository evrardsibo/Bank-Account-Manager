count = [ ]
class Coustomrs :
    def __init__(self , first_name , last_name , age , date) :
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.count = count
        self.date = date

    def create_account(self , account_number) :
        self.count.append( account_number )

    # def balence(self) :
    #     return sum( self.count )

    # def __str__(self) :
    #     return self.first_name + self.last_name + self.age + self.bank.name
