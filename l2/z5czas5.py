import datetime
word='alfabetagamma'
s=input('co policzyć? ') #s to szukana literka
start=datetime.datetime.now()
print (word.count(s))
czas = datetime.datetime.now()-start
print (czas)
