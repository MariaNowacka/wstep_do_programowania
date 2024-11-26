def fib(n):
    wynik=0
    if n==0:
        #tab.append(0)
        return 0
    if n==1:
        #tab.append(1)
        return 1
    if n>=2:
        tab.append('')
        wynik=fib(n-1)+fib(n-2)
        tab[n]=wynik
        return tab
    
n=int(input('ile cyfr podac? '))

tab=[0,1]
print(fib(n))

