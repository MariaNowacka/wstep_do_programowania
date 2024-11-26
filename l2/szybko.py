def fib(n):
    wynik=0
    tab=[0,1]
    if n==0:
        return 0
    if n==1:
        return 1
    if n>=2:
        tab.append('')
        wynik=str(fib(n-1)+fib(n-2))
        tab[n]=str(wynik)
        return tab

n=int(input('ile liczb podać: '))
print(fib(n))
