# before * only positional arguments are allowed.
# after / positional or named arguments are allowed.
# after * only named arguments are allowed. Must be named when calling the function

# // -> integer division
# ** exponentiation operator

x = 3
y = 2
def add_nums(x , y):
    z = x + y
    return z

print("result: ", add_nums(x,y))