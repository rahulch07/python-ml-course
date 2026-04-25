# from typing import override
from typing_extensions import override
from Account import Account

class SavingAccount(Account):

    @override
    def withdraw(self, amount, description):
        if self.balance - amount < 10000: 
            print("Insufficient Balance")
            return

        super().withdraw(amount, description)

# ac2 = SavingAccount(account_number= 2222, holder_name="Rohit", balance=50000)
# ac2.withdraw(10000, "EMI")
# ac2.withdraw(10000, "Loan")
# ac2.deposit(10000, "Business")
# ac2.print_statement()