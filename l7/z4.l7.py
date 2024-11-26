import random
import math
import matplotlib.pyplot as plt
import numpy as np
class Rocket:
    def __init__(self, Name,x=0,y=0):
       self.x=x
       self.y=y
       self.Name=Name
       self.paliwo = 20
       self.points = 0  
    cel=7

    def move(self,x,y):
        self.x+=x
        self.y+=y

    def get_position(self):
        return f'{self.x},{self.y}'

    def get_distance(self,other):
        a=self.x-other.x
        b=self.y-other.y
        return math.sqrt(a**2+b**2)

    def __str__(self):
        return f'{self.Name} {self.x}, {self.y}'
    
    def add(self,a):
      ''' funkcja dodaje podaną liczbę punktów użytkownikowi (lub odejmuje jeśli liczba jest ujemna)
          input : ilość punktów'''
      self.points+=a
    
    def go_to(self,x=0,y=0):
      ''' funkcja teleportuje rakietę w miejsce o podanych współrzędnych
          input : współrzędne punktu, do którego teleportujemy rakietę'''
      self.x=x
      self.y=y
    
def akcja():
  if rakieta.get_distance(p0)<3: 
    print('Dostajesz 2 punkty')
    rakieta.add(2)
  if rakieta.get_distance(p1)<1:
    print('Dostajesz paliwo : 1')
    rakieta.paliwo+=1
  if rakieta.get_distance(p2)<2:
    print('Zostałeś zaatakowany, odebrano ci 3 punkty i straciłeś paliwo : 2')
    rakieta.add(-3)
    rakieta.paliwo-=2
  if rakieta.get_distance(p3)<1:
    print('Rakieta zepchnęła Cię w róg planszy')
    rakieta.go_to(-10,-10)
  if rakieta.x==rakieta.y:
    print('Niespodzianka, zdobywasz punkt!')
    rakieta.add(1)
  if rakieta.get_distance(p0)==0:
    print('Otrzymujesz 4 punkty')
    rakieta.add(4)
  if rakieta.x>10 or rakieta.x<-10 or rakieta.y>10 or rakieta.y<-10:
    print('Nie uciekaj z planszy')
    rakieta.go_to()
    
rakieta=Rocket('name')    
name=input('podaj imię gracza: ')
rakieta.Name=name
print(f'Witaj {rakieta.Name}, Twoim celem jest zdobycie {rakieta.cel} punktów. W tym momencie masz {rakieta.points} punktów. Powodzenia!')
p0=Rocket('green',-5,-5)
p1=Rocket('yellow',-2,3)
p2=Rocket('orange',4,-6)
p3=Rocket('red',6,4)
def kolo(a,b,q,r=1):
  if q==0: c='green'
  if q==1: c='yellow'
  if q==2: c='orange'
  if q==3: c='red'
  x=np.arange(a-r,a+r,0.01)
  y=[]
  for i in x:
    y.append(abs(r**2-(i-a)**2)**0.5+b)
  for i in x[::-1]:
    y.append(-(abs(r**2-(i-a)**2)**0.5)+b)
  x=list(x)+list(x[::-1])
  plt.plot(x,y,color=c)
  plt.scatter(a,b,color=c)
def wykr():
  kola()
  plt.scatter(rakieta.x,rakieta.y,color='purple')
  plt.plot(-10,-10,10,10)
  plt.show()
def kola():
  kolo(-5,-5,0,3)
  kolo(-2, 3,1)
  kolo( 4,-6,2,2)
  kolo( 6, 4,3)
kola()
wykr()
print('Na planszy widzisz 5 rakiet, fioletowa jest Twoja. Pozostałe 4 mogą dać Ci punkty lub paliwo, zaatakować Cię lub zepchnąć w pewne miejsce jeśli znajdziesz się w ich zasięgu')
print('Lataj rakietą i zbieraj punkty (przesuwasz się wzdłuż osi x i y, zaraz zostaniesz poproszony o podanie ich wartości)')
while rakieta.paliwo>0:
  x,y = float(input('podaj wektor x ')), float(input('podaj wektor y '))
  rakieta.move(x,y)
  rakieta.paliwo-=(abs(x)+abs(y))//4
  akcja()
  wykr()
  print(f'Pozostałe paliwo : {rakieta.paliwo}')
  print(f'Twoje punkty : {rakieta.points}')
  if rakieta.points>=7:
    o=input('Cel został osiągnięty. Czy chcesz kontynuować gre? [t/n]')
    if o=='t':
      pass
    if o=='n':
      break

if rakieta.points<7:
  print('Niestety nie udało ci się osiągnąć celu :(')
else:
  print(f'Brawo {rakieta.Name}, kończysz grę z wynikiem {rakieta.points}')
