class Account:

    def __init__(self,owner, date, solde):
        self.owner = owner
        self.date = date
        self.interset = 0.01
        self.solde = solde
    
    def recieve_interset(self):
        self.solde += self.solde * self.interset