import math
print('podaj współczynniki trójmianu kwadratowego postaci ax^2 + bx + c = 0')
a=float(input('podaj a: '))
b=float(input('podaj b: '))
c=float(input('podaj c: '))
print(f'{a}*x^2 + {b}*x + {c} = 0')

if a==0:
  print(f'wynik tego dwumianu to : {-c/b}')
else:
    delta=b**2-(4*a*c)
    if (delta< 0):
        print('trójmian nie ma rozwiązań w zbiorze liczb rzeczywistych')
    if (delta==0):
        x0=-b/2/a
        print('x0 = ',x0)
    if (delta>0):
        x1=(-b-math.sqrt(delta))/2/a
        x2=(-b+math.sqrt(delta))/2/a
        print('x1 = ',x1, '\nx2 = ',x2)
