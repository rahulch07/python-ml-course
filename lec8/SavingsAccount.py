
from Account import Account


class SavingdAccount(Account):

    
    def withdraw(self, amount, description):
        if self.balance - amount < 10000:
            print("Insufficient Balance")
        else:
            super().withdraw(amount, description)