import matplotlib.pyplot as plt
f = open('ang.txt')
x = f.read()
f.close
x.lower()
ilosc=[]
for i in range (97,123):
  ilosc.append(0)
  ilosc[i-97]=x.count(chr(i))
litery = []
for i in range (97,123):
  litery.append(chr(i))
plt.bar(litery,ilosc)
plt.ylabel('ilość liter w tekście')
plt.xlabel('litery')
plt.title('występowanie poszczególnych liter w tekście')
plt.show()
print(litery)
print(ilosc)
