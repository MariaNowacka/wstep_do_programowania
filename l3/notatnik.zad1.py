#import matplotlib.pyplot as plt
f = open('ang.txt')
x = f.read()
f.close
print(x)
'''
a=x.count('a')
print (a)
l=[]
l.append(['a',a])
print(l)
b=x.count('b')
l.append(['b',b])
plt.hist(l, bins=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','r','s','t','u','w','x','y','z'])
plt.show()'''

'''
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

fruits = ['apple', 'blueberry', 'cherry', 'orange']
counts = [40, 100, 30, 55]
bar_labels = ['red', 'blue', '_red', 'orange']
bar_colors = ['tab:red', 'tab:blue', 'tab:red', 'tab:orange']

ax.bar(fruits, counts, label=bar_labels, color=bar_colors)

ax.set_ylabel('fruit supply')
ax.set_title('Fruit supply by kind and color')
ax.legend(title='Fruit color')

plt.show()


a=x.count('a')+x.count('A')
b=x.count('b')+x.count('B')
c,d=x.count('c'),x.count('d')
litery = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
powt = [a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z]
slownik = {'a':a, 'b': b}
print(slownik)
bars = [a,b]
plt.hist(slownik, bars, histtype = 'bar')
#plt.ylabel('liczba powtórzeń')
#plt.xlabel('litery')
plt.show()
'''
'''
#litery = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
'''
