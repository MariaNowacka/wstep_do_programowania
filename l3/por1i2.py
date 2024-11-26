import matplotlib.pyplot as plt
f = open('Tekst.angielski.17_05.txt')
x = f.read()
f.close
x.lower()
f = open('Tekst.polski.17_05.txt')
y = f.read()
f.close
ilosc=[]
for i in range (97,123):
  ilosc.append(0)
  ilosc[i-97]=x.count(chr(i))-y.count(chr(i))
ilosc.append(x.count('ą')-y.count('ą'))
ilosc.append(x.count('ć')-y.count('ć'))
ilosc.append(x.count('ę')-y.count('ę'))             
ilosc.append(x.count('ł')-y.count('ł'))
ilosc.append(x.count('ń')-y.count('ń'))
ilosc.append(x.count('ó')-y.count('ó'))
ilosc.append(x.count('ś')-y.count('ś'))
ilosc.append(x.count('ź')-y.count('ź'))
ilosc.append(x.count('ż')-y.count('ż'))
litery = []
for i in range (97,123):
  litery.append(chr(i))
litery = litery + ['ą','ć','ę','ł','ń','ó','ś','ź','ż']
plt.bar(litery,ilosc)
plt.ylabel('porównanie ilości liter w tekstach')
plt.xlabel('litery')
plt.title('porównanie tekstu angielskiego i polskiego')
plt.show()
