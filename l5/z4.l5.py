def fib(n):
    tab.append(0)
    tab.append(1)
    for i in range (2,n):
        tab.append(tab[i-2]+tab[i-1])
    return tab
    
tab=[]
n=int(input('ile wyrazów ciagu Fibonacciego podać? '))
print(fib(n))
