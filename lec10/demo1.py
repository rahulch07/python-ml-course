from itertools import zip_longest
from math import sqrt


letters = ['A', 'B', 'C', 'D']

# it = enumerate(letters)
# for (num, val) in it:
#     print(num, val)

digits = [1,2,3,4,5 ,6]

# for tup in zip(digits, letters): for equal tuples
#     print(tup)

for tup in zip_longest(digits, letters, fillvalue="NAN"): # for unequal tuples and fillvalue fill None
    print(tup)

#lambda: can only be simple line
class Mathclass:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def add(self):
        return self.a + self.b
    
    def func(self, operation):
        return operation(self.a, self.b)

m1 = Mathclass(2,3)
print(m1.add())

print(m1.func(lambda x, y: x-y))

print(list(map(lambda x: x**2, [1,2,3])))

def squareRoot(x):
    return sqrt(x)

print(list(map(squareRoot, [1,2,3])))

print(list(filter(lambda x: x>=2, [1,2,3])))

print("-"*30)

print(list(map(lambda x: x**2, [1,2,3]))) # will print till infinity because of list()

for val in map(lambda x: x**2, [1,2,3]): # # will print till where we want
    print(val)
    if val ==4: break
