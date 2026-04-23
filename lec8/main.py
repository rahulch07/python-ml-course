from SavingsAccount import SavingdAccount
from CurrentAccount import CurrentAccount



ac1 = SavingdAccount(1111, "Rahul", 1000000)
ac1.withdraw(10000, "EMI")

ac2 = CurrentAccount(2222, "Rohit", 10001)
ac2.withdraw(10000, "EMI")