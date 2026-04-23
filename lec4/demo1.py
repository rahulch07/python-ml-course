# lst = [0] * 5 gives list of 5 elements -> [0,0,0,0,0]

# List Comprehenshen

#               transformer            iterator                filter
lst = [val if val > 5 else -1 for val in range(1,10) if val % 2 == 0]
print(lst)