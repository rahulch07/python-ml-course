class Account:

    def __init__(self, *, account_number, holder_name, balance=0.0):
        self._account_number = account_number
        self.holder_name = holder_name
        self.__balance = balance

    def print(self):
        print(f"Account Number: {self._account_number}")
        print(f"Holder Name: {self.holder_name}")
        print(f"Balance: {self.__balance}")

ac1 = Account(account_number=1111, holder_name="Rahul", balance=1000000)
ac1.print()