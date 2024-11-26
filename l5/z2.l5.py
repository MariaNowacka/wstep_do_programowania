k=input('podaj kolor w html: ')
while len(k)!=7 or k[0]!='#':
    print('podano zły format, spróbuj jeszcze raz: ')
    k=input('podaj kolor w html: ')          
          
r=list(k[1:3])
g=list(k[3:5])
b=list(k[5:7])

def rgb(r,g,b):
    nr=int(r[0],16)*16+int(r[1],16)
    ng=int(g[0],16)*16+int(g[1],16)
    nb=int(b[0],16)*16+int(b[1],16)
    return (nr,ng,nb)

print(rgb(r,g,b))
