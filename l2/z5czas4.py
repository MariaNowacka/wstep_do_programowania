import datetime
word='alfabetagamma'
s=input('co policzyć? ') #s to szukana literka
suma=0
start=datetime.datetime.now()
for i in range (len(word)):
    if word[i]==s:
        suma=suma+1
print (suma)
czas = datetime.datetime.now()-start
print (czas)
