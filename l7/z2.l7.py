import random
import math
import matplotlib.pyplot as plt
class Rocket:
    def __init__(self, Name,x=0,y=0):
      # funkcja tworzy obiekt i inicjalizuje jego położenie
      # input : imię rakiety, współrzędne 
      self.x=x
      self.y=y
      self.Name=Name

    def move(self,x,y):
      # funkcja przesuwa rakietę o podany wektor
      # input : x - przesunięcie względem osi x
      #         y - przesunięcie względem osi y
      self.x+=x
      self.y+=y

    def get_position(self):
      # funkcja zwraca aktualną pozycję rakiety
      return f'{self.x},{self.y}'

    def get_distance(self,other):
      # funkcja oblicza odległość międzzy dwiema rakietami
      # input : self - pierwsza rakieta
      #         other - druga rakieta
      # output : odległość między pierwszą a drugą rakietą
      a=self.x-other.x
      b=self.y-other.y
      return math.sqrt(a**2+b**2)

    def __str__(self):
      # funkcja print
      # output : imię i współrzędne rakiety
      return f'{self.Name}, {self.x}, {self.y}'

rakieta=Rocket("Alex",2,4)
x=[]
y=[]
for i in range (5):
  a=random.randint(-5,5)
  b=random.randint(-5,5)
  rakieta.move(a,b)
  x.append(rakieta.x)
  y.append(rakieta.y)
  print(rakieta.get_position())
plt.plot(x[0::],y[0::],"--")
plt.plot(-5,-5, 5,5)
for i in range (0,5):
  plt.annotate(f'{i+1}',  xy=(x[i],y[i]))
plt.show()
  
#print(x,y)
