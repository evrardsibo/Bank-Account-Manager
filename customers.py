count = [ ]
class Coustomrs :
    def __init__(self , first_name , last_name , age , date,banque) :
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.count = count
        self.date = date

    def create_account(self , account_number) :
        self.count.append( account_number )
        return self.count
    def delete_account(self , account_number) :
        self.count.remove( account_number )
        return self.count
    def money_deposit(self):
        pass
    def money_withdraw(self):
        pass
    def money_transfer(self):
        pass
    def money_repay(self):
        pass
    def check_balance(self):
        pass

