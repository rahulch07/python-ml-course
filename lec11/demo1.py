# def fib():
#     x, y = 0,1
#     while True:
#         yield x
#         x, y = y, y+x
# f = fib()
# for _ in range(10):
#     print(next(f))

# this does not materilize the item unlike list
from itertools import islice


# lst = [1,2,3,4,5,6,7,8,9,10]

# print(lst[0: 9: 2]) # makes another copy of list in memory [1,3,5,7,9] so more memory

# for v in islice(lst, 0,9,2): # does not makes copy
#     print(v)


# head 
def head(fileName, lines=5):
    with open(fileName, 'r') as file:
        for line in islice(file, 0, lines):
            print(line)
# head("testing.txt")

# Slots : cannot add extra fields i.e. no monkey-patching
class Testing:

    __slots__ = ['name', 'id']


    def __init__(self, name: str, id: int):
        self.name = name
        self.id = id
    
    def display(self):
        print(f"name: {self.name}, id: {self.id}")

# obj = Testing("Rahul", "7")
obj = Testing("Rahul", 7)
obj.display()