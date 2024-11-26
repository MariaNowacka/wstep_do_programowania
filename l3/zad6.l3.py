n=int(input('Podaj liczbę wierzy: '))
while n==0:
  n=int(input('Podaj liczbę większą od zera: '))
p=[]
i = 0
for i in range (i, n):
  p.append([])
  p[i].append(1)
  for j in range (1,i):
    p[i].append(p[i-1][j-1]+p[i-1][j])
  p[i].append(1)
for i in range (n):
  print('  '*(n-i),end=' ')
  for j in range (0,i+1):
    print('{0:4}'.format(p[i][j]),end=' ')
  print()
