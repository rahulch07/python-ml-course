# def add(a: int, b: int):
#     return a+b

# c = add(1,"dsds")
# print(c)

from typing import TypeVar

T = TypeVar('T', int, str)

def add(a: T, b: T) -> T:
    return a+b
c = add(1,2)
print(c)

def add2[T :(int, str)](a: T, b: T) -> T:
    return a+b
c = add2(1,2)
print(c)