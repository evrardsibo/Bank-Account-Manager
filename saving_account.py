from datetime import datetime

import account


class Saving(account):
    def prime(self):
        if datetime.now().date() == self.date.date():
            self.solde += 0.50
