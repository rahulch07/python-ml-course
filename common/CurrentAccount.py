from typing_extensions import override

from Account import Account


class CurrentAccount(Account):

    @override
    def withdraw(self, amount, description):
        if self.balance - amount < 0:
            print("Overdraft limit reached")
        else:
            super().withdraw(amount, description)