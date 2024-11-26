import numpy as np
import matplotlib.pyplot as plt
import math 

def silnia(i):
    if i>1:
        return i*silnia(i-1)
    return 1

def pot_e (x,N):
    i=0
    wynik=0
    for i in range (N):
        wynik=wynik+ (x**i/silnia(i))
    return wynik

x=10
N=60
print('dla x=10: ',pot_e(10,N))
print('dla x=2: ',pot_e(2,N))
print('dla x=-2: ',pot_e(-2,N))
print('dla x=-10: ',pot_e(-10,N))

a=[]
for i in range (60):
  a.append(abs((math.exp(2)-(pot_e(2,i)))/math.exp(2)))
b=range(1,61)
a1=[]
for i in range (60):
  a1.append(abs((math.exp(-2)-(pot_e(-2,i)))/math.exp(-2)))

plt.plot(b, a, color='blue')
plt.plot(b,a1,color='orange')
plt.yscale('log')
plt.title('wykres dla x = 2 i x=-2')
plt.show()

c=[]
for i in range (60):
  c.append(abs((math.exp(10)-(pot_e(10,i)))/math.exp(10)))
c1=[]
for i in range (60):
  c1.append(abs((math.exp(-10)-(pot_e(-10,i)))/math.exp(-10)))

plt.plot(b, c, color='green')
plt.plot(b,c1,color='red')
plt.yscale('log')
plt.title('wykres dla x = 10 i x=-10')
plt.show()

# dla ujemnych x obliczamy ułamek 1/e**x,
# a wspomniany przy zadaniu 1 standard IEEE754 ma ograniczone możliwości
# przedstawiania tak małych liczb (w pojedynczej precyzji dokładność p=24
# w podwójnej p=53
