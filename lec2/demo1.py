def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):  # iterates till end... not necessary
        if n % i == 0:
            return False
    return True

def is_prime2(num):
    if num <=1:
        return False
    for i in range(2, num//2 + 1):  # just to optimize the loop, we can check only till num//2
        if num % i == 0:
            return False
    return True

num = 2
max = 10

while num <= max:
    if not is_prime2(num):
        num += 1
        continue
    print(num)
    num += 1

# trying docstrings
def add_two_numbers(a,b):
    "docstring: this function adds two numbers"
    return a + b
# print("add_two_numbers(2,3) = ", add_two_numbers(2,3))

# fibonacci series
def fibonacci(num):
    if num <= 0:
        print("number should be greater than 0")
        return
    elif num == 1:
        print(0)
        return
    sum, next = 0,1
    while sum < num:
        print(sum, end=' ')
        sum , next = next, sum + next
# fibonacci(2)

#named arguments
def print_name(name, age):
    print("name: ", name)
    print("age: ", age)

print_name(age=30, name="Alice")

# variable arguments
def print_numbers(*args, length):
    print("length: ", length)
    for num in args:
        print(num, end=',')
print_numbers(1,2,3,4,5, length=5)

print("\n")

# kwargs
def print_info(length, **kwargs):
    print("length: ", length)
    for key, value in kwargs.items():
        print(f"{key}: {value}")
print_info(name="Alice", age=30, city="New York", length=3)