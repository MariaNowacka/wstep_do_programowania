slowo=input('podaj słowo: ')
slowo=slowo.lower()
a=len(slowo)
spr=0
for i in range (a):
    if slowo[i]==slowo[a-1-i]:
        spr=spr+1

if spr==a:
    print('słowo jest palindromem')
else:
    print('podane slowo nie jest palindromem')        
    

             
