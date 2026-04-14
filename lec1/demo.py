import sys

# list is like an array but it can hold different types of data and it is mutable (can be changed after creation). It is a built-in data structure in Python.
lst = ["a", "b", "c", "d", "e"]
print(lst)
print(lst[0])
print(type(lst), sys.getsizeof(lst))

# tuple is like a list but it is immutable (cannot be changed after creation). It is also a built-in data structure in Python.
tup = ("a", "b", "c", "d", "e")
print(tup)
print(tup[0])
print(type(tup), sys.getsizeof(tup))

# set is an unordered collection of unique elements. It is a built-in data structure in Python.
st = {"a", "b", "c", "d", "e"}
print(st)
print(type(st), sys.getsizeof(st))

# dictionary is a collection of key-value pairs. It is a built-in data structure in Python. like Map, HashMap, HashTable.
dct = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
print(dct)
print(dct["a"])
print(type(dct), sys.getsizeof(dct))

# id
a = 1
print(a, sys.getsizeof(a), id(a))
b = 2
print(b, sys.getsizeof(b), id(b))

a = a+1
print(a, sys.getsizeof(a), id(a))
c = 2
print(c, sys.getsizeof(c), id(c))

d = "jdjsldjsakdjaskdjsalkdjsakd"

# reference count
print(sys.getrefcount(d))