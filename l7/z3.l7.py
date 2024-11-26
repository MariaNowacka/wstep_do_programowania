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
        return f'{self.Name} {self.x}, {self.y}'

tabx=[]
taby=[]
for i in range (5):
  tabx.append(random.randint(-5,5))
  taby.append(random.randint(-5,5))                
rakieta1=Rocket("Anne",tabx[0],taby[0])
print(rakieta1)
rakieta2=Rocket("Bella",tabx[1],taby[1])
print(rakieta2)
rakieta3=Rocket("Cindy",tabx[2],taby[2])
print(rakieta3)
rakieta4=Rocket("Dorothy",tabx[3],taby[3])
print(rakieta4)
rakieta5=Rocket("Eleanor",tabx[4],taby[4])
print(rakieta5)

flota=[rakieta1,rakieta2,rakieta3,rakieta4,rakieta5]

plt.scatter(tabx,taby, color='purple')
plt.annotate('A',  xy=(tabx[0],taby[0]))
plt.annotate('B',  xy=(tabx[1],taby[1]))
plt.annotate('C',  xy=(tabx[2],taby[2]))
plt.annotate('D',  xy=(tabx[3],taby[3]))
plt.annotate('E',  xy=(tabx[4],taby[4]))
plt.plot(-15,-15, 15,15)
plt.title('pozycje początkowe')
plt.show()
print('\n')
for i in range (4):
  tx=[]
  ty=[]
  for obj in flota:
    x,y=random.randint(-5,5),random.randint(-5,5)
    obj.move(x,y)
    print(obj)
    tx.append(obj.x)
    ty.append(obj.y)
  plt.scatter(tx,ty, color='blue')
  plt.annotate('A',  xy=(tx[0],ty[0]))
  plt.annotate('B',  xy=(tx[1],ty[1]))
  plt.annotate('C',  xy=(tx[2],ty[2]))
  plt.annotate('D',  xy=(tx[3],ty[3]))
  plt.annotate('E',  xy=(tx[4],ty[4]))
  plt.title(f'{i+1} przesunięcie')
  plt.plot(-15,-15, 15,15)
  plt.show()
  for i,obj in enumerate (flota[1:]):
    print(f'odległość między 1 i {i+2} : {rakieta1.get_distance(obj)}')
  for i,obj in enumerate (flota[2:]):
    print(f'odległość między 2 i {i+3} : {rakieta2.get_distance(obj)}')
  for i, obj in enumerate (flota[3:]):
    print(f'odległość między 3 i {i+4} : {rakieta3.get_distance(obj)}')
  print(f'odległość między 4 i 5 : {rakieta4.get_distance(rakieta5)}\n')
    
