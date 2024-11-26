import random
import math
class Rocket:
    def __init__(self, Name,x=0,y=0):
      ''' funkcja tworzy obiekt i inicjalizuje jego położenie
          input : imię rakiety, współrzędne '''
      self.x=x
      self.y=y
      self.Name=Name

    def move(self,x,y):
      ''' funkcja przesuwa rakietę o podany wektor
          input : x - przesunięcie względem osi x
                  y - przesunięcie względem osi y '''
      self.x+=x
      self.y+=y

    def get_position(self):
      ''' funkcja zwraca aktualną pozycję rakiety '''
      return f'{self.x},{self.y}'

    def get_distance(self,other):
      ''' funkcja oblicza odległość między dwiema rakietami
          input : self - pierwsza rakieta
                  other - druga rakieta
          output : odległość między pierwszą a drugą rakietą '''
      a=self.x-other.x
      b=self.y-other.y
      return math.sqrt(a**2+b**2)

    def __str__(self):
      ''' funkcja print
          output : imię i współrzędne rakiety'''
      return f'{self.Name}, {self.x}, {self.y}'
