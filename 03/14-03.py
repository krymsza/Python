#zad1

class Complex(object):
  
  def __init__(self, a, b):
    self.a = a
    self.b = b 
    
  def __add__(self, number):
    if(type(number) == type(self)):
      result = Complex(self.a + number.a, self.b + number.b)
    else:
      result = self
      result.a = self.a + number
    return result
    
  def __sub__(self, number):
    if(type(number) == type(self)):
      result = Complex(self.a - number.a, self.b - number.b)
    else:
      result = self
      result.a = self.a - number
    return result
    
  def __mul__(self, number):
    if(type(number) == type(self)):
      result = Complex(self.a * number.a, self.b * number.b)
    else:
      result = self
      result.a = self.a * number
    return result
    
  def __truediv__(self, number): 
    if(type(number) == type(self)): 
      result = Complex(self.a / number.a, self.b / number.b)
      return result
    else:
      result = self
      result.a = self.a / number
      return result
    
  def modul(self):
    return self.a**0.5 + self.b**0.5
    
  def __eq__(self, number):
    if (number.modul() == self.modul()):
      return True
    else:
      return False
      
  def __lt__(self, number):
    if(number.modul() < self.modul()):
      return True
    else:
      return False
      
  def __le__(self, number):
    if(number.modul() < self.modul()):
      return True
    else:
      return False

  def __str__(self):
    return " %s + %si " % (self.a, self.b)
    
num1 = Complex(5,8)
num2 = Complex(3,0)
num3 = num1 - num2
print (num3)
print (num3 + num1) 
print (num1 - num1) 
print (num3 * 2) 
print (num2 * num1)
print (num1 / num1)
print (num1 > num3)
print (num1 < num3)
print (num1 == num3)




#zad2

class Point2D(object):
  def __init__(self, x=0, y=0):
    self.x=x
    self.y=y
  def distance(self, other):
    return( (other.x - self.x)**2 + (other.y - self.y)**2 )**0.5
    
class Pint3D(Point2D):
  def __init__(self,x=0 ,y=0, z=0):
    super().__init__(x,y)
    self.z=z
  def distance(self, other):
    return( (other.x - self.x)**2 + (other.y - self.y)**2 + (other.z - self.z)**2 )**0.5

point = Point2D(2,0)
other = Point2D()
print(point.distance(other))




#zad3
