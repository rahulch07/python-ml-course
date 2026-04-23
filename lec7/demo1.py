def add(a, b):
    c = a + b
    return c

def main():
    x = 2
    y = 3

    result = add(x, y)
    print(result)

class testing:
    def __init__(self, val):
        self.val = val

    def display(self):
        print(f"Value is: {self.val}")

# main()
# obj = testing(10)
# obj.display()


def func2():
    yield 1
    yield 2
    yield 3

# print(func2())
# for val in func2():
#     print(val)

it = iter(func2())

print(next(it))
print(next(it))
print(next(it))
# print(next(it))

# for val in (value for value in range(1,100)):
#     print(val)

[print(value) for value in range(1,100)]