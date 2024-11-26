i=3
x=1
l=1
for l in range(10):
    if l<1 or l>=8:
        print(" "*2,"*")
    else:
         while l<3:
             while i<=5:
                 print(int((5-i)/2)*" ",i*"*")
                 i=i+2
             i=3
             l=l+1

