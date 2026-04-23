from Account import Account


class CurrentAccount(Account):
    def withdraw(self, amount, description):
        if self.balance - amount < 0:
            print("Overdraft limit reached")
        else:
            super().withdraw(amount, description)

