def szyfr(x):
    y=''
    for i in range (len(x)):
        if (ord(x[i])>=97 and ord(x[i])<110) or (ord(x[i])>=65 and ord(x[i])<77):
            c = ord(x[i])
            c += 13
            y = y + chr(c)
        elif ord(x[i])>=109 and ord(x[i])<123  or (ord(x[i])>=77 and ord(x[i])<91):
            d = ord(x[i])
            d -= 13
            y = y + chr(d)
        else:
            d = ord(x[i])
            y = y + chr(d)
    return y
        
x=input('podaj tekst: ')
print(szyfr(x))
