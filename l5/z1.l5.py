r=input('podaj r w tryplecie rgb: ')
g=input('podaj g w tryplecie rgb: ')
b=input('podaj b w tryplecie rgb: ')

def a(r):
    if len(r)<4:
        if len(r)==3:
            r='0'+r
    return r

r=hex(int((r)))
g=hex(int((g)))
b=hex(int((b)))

def a(r):
    if len(r)<4:
        if len(r)==3:
            r=r[0:2]+'0'+r[-1]
    return r

r=a(r)
b=a(b)
g=a(g)

def tlumacz(r,g,b):
    nowy='#'+r[2:]+g[2:]+b[2:]
    return nowy

#print (r,g,b)
print(tlumacz(r,g,b))
