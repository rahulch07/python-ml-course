class Account:
    def __init__(self, acc_num: int, name: str, balance: float=0.0):
        self.name = name
        self.balance = balance
        self.acc_num = acc_num
        self.transactions: list[tuple[str, float, str]] = [] # while defining () is not used 
    
    def deposit(self, amount, description):
        self.balance += amount

        txn = (description, amount, "CR")
        self.transactions.append(txn)
    
    def withdraw(self, amount, description):
        self.balance -= amount

        txn = (description, amount, "DB")
        self.transactions.append(txn)

    def print_statement(self):
        print(self.__class__.__name__)
        print("-"*30)
        print(f"Account Holder: {self.name}")
        print(self.balance)
        print("-"*30)
        for txn in self.transactions:
            print(f"{txn[0]: ^15} {txn[1]: ^10} {txn[2]: ^5}")

class SavingAccount(Account):
    def withdraw(self, amount, description):
        if self.balance - amount < 10000: print("Insufficient Balance")

        super().withdraw(amount, description)


# ac1 = Account(1111, "Rahul", 1000000)
# ac1.deposit(100000, "April salary")
# ac1.deposit(100000, "May salary")

# ac1.print_statement()

# ac2 = SavingAccount(2222, "Rohit", 50000)
# ac2.withdraw(10000, "EMI")
# ac2.print_statement()


# Method Resolution Order (for multiple inheritance)
class Class1:
    def func(self):
        print("Class1")

class Class2(Class1):
    def func(self):
        print("Class2")

class Class3(Class1):
    def func(self):
        print("Class3")

class Class4(Class3, Class2):
    # def func(self):
    #     print("Class4")
    pass

obj = Class4()
obj.func()

print(Class4.mro())