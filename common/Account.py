from abc import ABC, abstractmethod


class Account(ABC):

    def __init__(self, *, account_number, holder_name, balance=0.0):
        self._account_number = account_number
        self.holder_name = holder_name
        self.__balance = balance
        self.transactions: list[tuple[str, float, str]] = [] # while defining () is not used 

    
    def __str__(self):
        return f"Account Number: {self._account_number}\nHolder Name: {self.holder_name}\nBalance: {self.__balance}"
    
    def __repr__(self):
        return f"Account({self._account_number}, {self.holder_name}, {self.__balance})"
    
    def __gt__(self, other):
        return self.__balance > other.__balance
    
    def __lt__(self, other):
        return self.__balance < other.__balance
    
    @property
    def balance(self):
        return self.__balance
    
    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("Balance cannot be negative")
        self.__balance = value

    @balance.deleter
    def balance(self):
        raise AttributeError("Balance cannot be deleted")
    
    def deposit(self, amount, description):
        self.balance += amount

        txn = (description, amount, "CR")
        self.transactions.append(txn)
    
    @abstractmethod
    def withdraw(self, amount, description):
        self.balance -= amount

        txn = (description, amount, "DB")
        self.transactions.append(txn)

    def print_statement(self):
        print(self.__class__.__name__)
        print("-"*30)
        print(f"Account Holder: {self.holder_name}")
        print(self.balance)
        print("-"*30)
        for txn in self.transactions:
            print(f"{txn[0]: ^15} {txn[1]: ^10} {txn[2]: ^5}")



# ac1 = Account(account_number=1111, holder_name="Rahul", balance=1000000)
# print(ac1)

# ac1.balance = 2000000
# print(ac1.balance)

# del ac1.balance
# print(ac1)