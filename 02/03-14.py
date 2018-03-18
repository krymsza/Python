-#zad1
-
-class Complex(object):
-  
-  def __init__(self, a, b):
-    self.a = a
-    self.b = b 
-    
-  def __add__(self, number):
-    if(type(number) == type(self)):
-      result = Complex(self.a + number.a, self.b + number.b)
-    else:
-      result = self
-      result.a = self.a + number
-    return result
-    
-  def __sub__(self, number):
-    if(type(number) == type(self)):
-      result = Complex(self.a - number.a, self.b - number.b)
-    else:
-      result = self
-      result.a = self.a - number
-    return result
-    
-  def __mul__(self, number):
-    if(type(number) == type(self)):
-      result = Complex(self.a * number.a, self.b * number.b)
-    else:
-      result = self
-      result.a = self.a * number
-    return result
-    
-  def __truediv__(self, number): 
-    if(type(number) == type(self)): 
-      result = Complex(self.a / number.a, self.b / number.b)
-      return result
-    else:
-      result = self
-      result.a = self.a / number
-      return result
-    
-  def modul(self):
-    return self.a**0.5 + self.b**0.5
-    
-  def __eq__(self, number):
-    if (number.modul() == self.modul()):
-      return True
-    else:
-      return False
-      
-  def __lt__(self, number):
-    if(number.modul() < self.modul()):
-      return True
-    else:
-      return False
-      
-  def __le__(self, number):
-    if(number.modul() < self.modul()):
-      return True
-    else:
-      return False
-
-  def __str__(self):
-    return " %s + %si " % (self.a, self.b)
-    
-num1 = Complex(5,8)
-num2 = Complex(3,0)
-num3 = num1 - num2
-print (num3)
-print (num3 + num1) 
-print (num1 - num1) 
-print (num3 * 2) 
-print (num2 * num1)
-print (num1 / num1)
-print (num1 > num3)
-print (num1 < num3)
-print (num1 == num3)
-
-
-
-
-#zad2
-
-class Point2D(object):
-  def __init__(self, x=0, y=0):
-    self.x=x
-    self.y=y
-  def distance(self, other):
-    return( (other.x - self.x)**2 + (other.y - self.y)**2 )**0.5
-    
-class Pint3D(Point2D):
-  def __init__(self,x=0 ,y=0, z=0):
-    super().__init__(x,y)
-    self.z=z
-  def distance(self, other):
-    return( (other.x - self.x)**2 + (other.y - self.y)**2 + (other.z - self.z)**2 )**0.5
-
-point = Point2D(2,0)
-other = Point2D()
-print(point.distance(other))
-
-
-
-
-#zad3
class Wheel(object):
  __tire_pressure = None
  __diameter= None
  
  def __init__(self,b=0):
    self.__tire_pressure  = True
    self.__diameter = b
    
  def capability_w(self, c):
    self.__tire_pressure = c
    
  def condition_w(self):
    if(self.__diameter == 100 and self.__tire_pressure == True):
      return True
    else:
      return False

class Engine(object):
  __power = None
  __efficiency = None
  
  def __E_init__(self, e, p):
    self.__efficiency = e
    self.__power = p
  
  def capability_e(self, e, p):
    self.__efficiency = e
    self.__power = p
    
  def condition_e(self):
    if(self.__efficiency == True and self.__power > 0):
      return True
    else:
      return False

class Details(object):
  __price = None
  __color = None
  __brand = None
  __year_of_production = None
  
  def ___D_init__(self, model, brand, yr):
    self.__model = model
    self.__brand = brand
    self.__year_of_production = yr
  
  def valuation(self):
    if(self.__year_of_production == 1967 and self.__brand == "Ford" and self.__model == "GT40 Lightweight"):
      return 11000000
    elif(self.__year_of_production < 1980):
      return 10000
    else:
      return 35000
      

class Car(Wheel, Engine, Details):
  __bought = False
  __new = None
  
  def __init__(self, diameter_W, efficiency_E, power_E, model, brand, yr, new):
    self.__bought = False
    self.__new = new
    super(Car, self).__init__(diameter_W)
    super(Car, self).__E_init__(efficiency_E, power_E)
    super(Car, self).___D_init__(model, brand, yr)
  
  def ability(self):
    if( super(Car, self).condition_e() == True and super(Car, self).condition_w() == True ):
     print("this car is working")
     return True
    else:
     print("this car needs to be repaired ")
     return False

  def buy(self, max_price, use):
    if(self.ability() == True and super(Car, self).valuation() <= max_price and self.__bought == False and use == self.__new):
      self.__bought = True
      print("You can buy this car!")
    else:
      print("UPS! You can't buy this car")



c = Car(100, True, 40, "GT40 Lightweight", "Ford", 1967, True)
c.ability()
c.buy(20000000, True)


