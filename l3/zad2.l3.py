import matplotlib.pyplot as plt
f = open('Tekst.polski.17_05.txt')
x = f.read()
f.close
x.lower()
ilosc=[]
for i in range (97,123):
  ilosc.append(0)
  ilosc[i-97]=x.count(chr(i))
ilosc.append(x.count('ą'))
ilosc.append(x.count('ć'))
ilosc.append(x.count('ę'))             
ilosc.append(x.count('ł'))
ilosc.append(x.count('ń'))
ilosc.append(x.count('ó'))
ilosc.append(x.count('ś'))
ilosc.append(x.count('ź'))
ilosc.append(x.count('ż'))
litery = []
for i in range (97,123):
  litery.append(chr(i))
litery = litery + ['ą','ć','ę','ł','ń','ó','ś','ź','ż']
plt.bar(litery,ilosc)
plt.ylabel('ilość liter w tekście')
plt.xlabel('litery')
plt.title('występowanie poszczególnych liter w tekście')
plt.show()
