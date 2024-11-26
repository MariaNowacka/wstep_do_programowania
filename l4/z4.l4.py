import numpy
import math
a=c=1
b=numpy.linspace(10**7.4, 10**8.5, num=100, endpoint=True)

#x1=1/2/a*(-i-math.sqrt(i**2-4*(a*c)))
#x2=1/2/a*(-i+math.sqrt(i**2-4*(a*c)))
#x3=c/a/x1

for i in b:
    x1=1/2/a*(-i-math.sqrt(i**2-4*(a*c)))
    print (f'dla b={i}\n wzór 1: \n  x1={1/2/a*(-i-math.sqrt(i**2-4*(a*c)))} \n  x2={1/2/a*(-i+math.sqrt(i**2-4*(a*c)))} \n wzór 2: \n  x1={1/2/a*(-i-math.sqrt(i**2-4*(a*c)))} \n  x2={c/a/x1}')

# bezpieczniejszy jest wzór drugi, w pierwszym wzorze bardzo małe wartości
# są zamieniane na 0 (utrata cyfr znaczących - zamiast 0,dużo 0 i jakieś cyfry
# większe od zera mamy 0)
