import math

x=9.8**201
y=10.2**199
#z1=math.sqrt(x**2 + y**2)
z2=y*math.sqrt((x/y)**2+1)
#print(z1)
print(z2)

# z1 wykracza poza zakres
# 1.8*10**308
# (9.8**201)**2 = 9.8**402 > 1.8*10**308
# (10.2**199)**2 = 10.2**398 > 1.8*10**308
