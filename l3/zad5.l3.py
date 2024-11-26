print('Dla ilu liczb szukasz największego wspólnego dzielnika? ')
n=int(input())
tab=[]
for i in range (n):
    a=int(input(f'podaj {i+1} liczbę: '))
    tab.append(a)
l=min(tab)
dzielniki = []
for i in range (1,l+1):
    if l%i==0:
        dzielniki.append(i)
a=len(dzielniki)
for i in range (n):
    for j in range (1,a):
        if int(tab[i]%int(dzielniki[a-1]))!=0:
            a=a-1        
    else:
        wynik = dzielniki[a-1]
print(f'nwd podanych liczb to: {dzielniki[a-1]}')
           
