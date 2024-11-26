w1=input('podaj pierwsze slowo: ')
w2=input('podaj drugie slowo: ')
if len(w2)>len(w1):
    a=w1
    w1=w2
    w2=a
if(len(w1)>len(w2)):
   w2=w2+' '*(len(w1)-len(w2))

    
for i in range(len(w1)):
       if w1[i]==w2[i]:
           print(i+1, 'Elementy są równe')
       else:
           print(i+1, 'Elementy są różne')
           
   
