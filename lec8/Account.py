from abc import abstractmethod


class Account():
    def __init__(self, acc_num: int, name: str, balance: float=0.0):
          self.name = name
          self.balance = balance
          self.acc_num = acc_num

    @abstractmethod
    def withdraw(self, amount, description):
          self.balance -= amount
          print(f"After ${description} balance remaining is ${self.balance}")