from typing_extensions import override

from Account import Account
from FixedDeposit import FixedDeposit



class FlexiDeposit(FixedDeposit):

    @override
    def withdraw(self, amount, description) -> None:
        if amount > self.balance:
            print("Cannot withdraw more than balance")
        
        if amount % 1000 != 0:
            print("Amount must be multiple of 1000")
        return Account.withdraw(self, amount, description)