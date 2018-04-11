#! /usr/bin/env
import math

def sqrt(x):
    try:
        res = math.sqrt(x)
        return res
    except(ValueError,TypeError) as e:
        print("nieoczekiwany błąd")
        print(e)
    else:
        print(res)
    finally:
        print("koniec funcji")
            
print (sqrt(3/4000))
print()
print (sqrt(4))
print()
print (sqrt(0.3535345))
print()
print (sqrt(-4))
print()
print (sqrt("test"))
