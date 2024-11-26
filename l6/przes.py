def przes(a,b=[1,1]):
  ''' funkcja przesuwa dysk (współrzędne środka dysku, na podstawie których można narysować dysk) o podany wektor
   input = parametry:
   a - pozycja poczatkowa
   b - wektor przesunięcia
   output:
   c - pozycja końcowa'''
  c=[a[0]+b[0],a[1]+b[1]]
  return c
