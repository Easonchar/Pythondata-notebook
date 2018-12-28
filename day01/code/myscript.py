import random

def foo(n):
    x = 0
    for i in range(n):
        x += random.randint(0,100)
        
    return x

A = 'abc'