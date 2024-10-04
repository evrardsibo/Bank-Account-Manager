from datetime import datetime


class Coustomrs:
    def __init__(self, first_name, last_name, age, banque):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.count = []
        self.date = datetime.now()
        self.banque = banque
        self.solde = 0

    def create_account(self, account_number):
        self.count.append(account_number)
        print("Your is created !")

    def delete_account(self, account_number):
        self.count.remove(account_number)
        print("Your is deleted !")

    def money_deposit(self, amount):
        self.solde += amount

    def money_withdraw(self, amount):
        if amount > self.solde:
            print("Insufficient funds")

        else:
            self.solde -= amount

    def money_transfer(self, amount, account):
        if amount > self.solde:
            print("Insufficient funds")
        else:
            self.solde -= amount
            account.solde += amount
    def money_transfer_otheraccount(self, amount, account_dest,my_account):
        if amount > self.solde:
            print("Insufficient funds")
        else:
            self.solde -= amount
            account_dest.solde += amount
            my_account.solde -= amount
    def check_balance(self):
        print(f"Your Balance is {self.solde}€")
