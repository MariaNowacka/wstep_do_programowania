import datetime
now = datetime.datetime.now()
def fib(n):
    if n==0:
        tab.append(0)
        return 0
    if n==1:
        tab.append(1)
        return 1
    if n>1:
        return fib(n-1)+fib(n-2)
    
tab=[]
n=40
for i in range (n):
    print(fib(i),end=' ')
czas1=datetime.datetime.now()-now
now2 = datetime.datetime.now()
def fib(n):
    tab.append(0)
    tab.append(1)
    for i in range (2,n):
        tab.append(tab[i-2]+tab[i-1])
    return tab
    
tab=[]
n=40
print(fib(n))
czas2=datetime.datetime.now()-now2
print(f'czas przy rekurencji: {czas1} /n czas przy iteracji: {czas2}')
