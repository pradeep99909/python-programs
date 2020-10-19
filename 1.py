from functools import reduce
a=[1,2,3,4,56]

def r(a, b):
    return a+b

print(reduce(r,a))