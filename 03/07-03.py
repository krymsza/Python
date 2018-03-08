
#notatki
liczby = range (0,20)
kwadraty = [x**2  for x in liczby]
print(kwadraty)
#----
def f1(n):
  def f2(x):
    return n -x
  return f2
    
res = f1(5)
print(f1(10))
#---
kwadrat = lambda x: x*x
print kwadrat(2)
#---
def generator(n):
  print("start")
  while n:
    print("Generator stop %d" % n)
    yield n
    print("Generator start %d" % n)
    n-=1
    
for x in generator(5):
   print( "wywolanie %d "  %x)

#----------------------------


# zadanie 1
napis = "ala ma kota"
lista = [(slowo, len(slowo)) for slowo in napis.split()]
print (lista)

#zadanie 2

def fibo(n):
    if(n<3):
        return 1
    else:
      return fibo(n-1)+ fibo(n-2)

n = input()
lista = [(fibo(i)) for i in range (1,n+1)]
print lista

#--------
n = input()
goldenRatio = (1+5**0.5)/2
fib = [int(( (goldenRatio)**i = (1 - goldenRatio)**i) / (5**0.5)) for in range (0,n)]
print (fib)
#--------


#zadanie 4

def Flog( x ):
  if(x % 3 == 0):
    return 1
  else:
    return 0

def F(Flog,lista):
    li = [(lista[i]) for i in range(0,len(lista)) if(Flog(lista[i]))]
    return li
    
lista = [2,6,3,78,4,0]
print(F(Flog, lista))

#zadanie 5 

#print(u"żółć żółą droga"[::2])
from  math import sqrt

def fun(lista, kontorlny):
  li =[]
  for i in range (0, len(lista)):
    li.append( ( sqrt( (lista[i][0] - kontorlny[0])**2 + (lista[i][1] - kontorlny[1])**2),   ((lista[i][0]), (lista[i][1])))  )
    
  li.sort()
  print (li)

lista = [ [2,0], [1,1], [4,8] ]
fun(lista, [0,0])

#zadanie 6 DOKONCZ NIE DZIALA
#! python
import sys, os
#path = input("Podaj sciezke ")
path="C:\"
dirs = os.listdir( string(path) )

for file in dirs:
	print file
