word='alfabetagamma'
s=input('co policzyć? ') #szukana literka
suma=0
for i in range (len(word)):
    if word[i]==s:
        suma=suma+1
print (suma)
    
