#zadanie1 

imie = input('podaj imie\n')
nazwisko = input('podaj nazwisko\n')
wiek = input('podaj wiek\n')
if( int(wiek) >=18):
    print('\nCzesc', imie, ' ', nazwisko, 'jestes pelnoletni!')
else:
    print('\nCzesc', imie , ' ', nazwisko, 'nie jestes pelnoletni')


#zadanie 2

l1 = input()
l2 = input()
l3 = input()

if( l1 > l2  and l1 > l3):
    print(l1)
elif(l2 > l1 and l2> l3):
    print(l2)
else: 
    print(l3)
    
#zadanie 3

mala = 97
duza = 65
n = input()
 
for i in range (0, 25):
    if( i % int(n) == 0):
         print( chr(mala) + " " + chr(duza))
    mala = mala + 1
    duza = duza + 1
    
    
#zadanie 4

n = input("podaj ile liczb\n ")
li = []

for i in range (0,int(n)):
  temp = input()
  li.append(temp)

li.sort()
x = input("wybierz: 0->sortowanie malejaco; 1->sortowanie rosnaco\n")

if(int(x) == 0):
  li.reverse()

print("podaj przedzialy do wyswietlenia ")
x=input()
y=input()
print(li[int(x):int(y)])

#zadanie 5

def fibo(n):
    if(n<3):
        return 1
    else:
        return fibo(n-1)+ fibo(n-2)
        
        
for i in range (0,10):
    print(fibo(i)," ")
