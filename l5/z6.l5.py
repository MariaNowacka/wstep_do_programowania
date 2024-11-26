l=input('podaj listę liczb: ').lower()

def fun(l):
    a=l.split(',')
    n=[]
    for i in range (len(a)):
        if a[i]!='':
            n.append(a[i])
    m=r=0
    for i in range (len(n)-1):
        if float(n[i])>float(n[i+1]):
            m=m+1
        if float(n[i])<float(n[i+1]):
            r=r+1
    a=[]    
    if m==0 and r==len(n)-1:
        print('lista jest posortowana rosnąco')        
        return (m==0 and r==len(n)-1) or (r==0 and m==len(n)-1)
    if r==0 and m==len(n)-1:
        print('lista jest posortowana malejąco')
        return (m==0 and r==len(n)-1) or (r==0 and m==len(n)-1)
    if (r!=len(n)-1 and m!=len(n)-1):
        return (m==0 and r==len(n)-1) or (r==0 and m==len(n)-1)

while len(l)==1:
    print('podano za mało argumentów')
    l=input('podaj listę liczb: ').lower()

c=0    
for i in range (len(l)):
    if (ord(l[i])>=97 and ord(l[i])<123):
        c=c+1
if c>0:
    print('podano literę')
if c==0:
    print(fun(l))
    




