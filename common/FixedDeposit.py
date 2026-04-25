from typing_extensions import override

from Account import Account


class FixedDeposit(Account):

    @override
    def withdraw(self, amount, description) -> None:
        raise Exception("Overdraft limit reached")