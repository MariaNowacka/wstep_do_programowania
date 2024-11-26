import random
import math
class Rocket:
    def __init__(self, Name,x=0,y=0):
             self.x=x
             self.y=y
             self.Name=Name
    def move(self,x,y):
        self.x+=x
        self.y+=y
    def get_position(self,x,y):
        return f'{self.x},{self.y}'

    def get_distance(self,other):
        a=self.x-other.x
        b=self.y-other.y
        return math.sqrt(a**2+b**2)
    def __str__(self):
        return f'{self.Name}, {self.x}, {self.y}'
tabx=[]
taby=[]
x=random.randint(-5,5)
y=random.randint(-5,5)                
rakieta1=Rocket("Anne",x,y)
tabx.append(x)
taby.append(y)
print(rakieta1)
rakieta1.move(1,2)
print(rakieta1)
x=random.randint(-5,5)
y=random.randint(-5,5)
rakieta2=Rocket("Bella",x,y)
tabx.append(x)
taby.append(y)
print(rakieta2)
print(rakieta1.get_distance(rakieta2))        
x=random.randint(-5,5)
y=random.randint(-5,5)
rakieta3=Rocket("Cindy",x,y)
tabx.append(x)
taby.append(y)
print(rakieta3)
x=random.randint(-5,5)
y=random.randint(-5,5)
rakieta4=Rocket("Dorothy",x,y)
print(rakieta4)
x=random.randint(-5,5)
y=random.randint(-5,5)
rakieta5=Rocket("Eleanor",x,y)
tabx.append(x)
taby.append(y)
print(rakieta5)
print(tabx,taby,sep='\n')


