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

print (sqrt(0.954)) 
print()
print (sqrt(9/700))
print()
print (sqrt("test"))
print()
print (sqrt(25))
print()
print (sqrt(-22))

