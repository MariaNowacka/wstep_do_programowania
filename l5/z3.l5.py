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
n=int(input('ile wyrazów ciągu Fibonacciego podać? '))
for i in range (n):
    print(fib(i),end=' ')
