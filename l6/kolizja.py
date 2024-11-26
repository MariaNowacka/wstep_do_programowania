def kolizja(x1,y1,x2,y2):
  ''' funkcja sprawdza czy między dwoma dyskami zachodzi kolizja
   input :
   parametry: x1 - float, pierwsza współrzędna pierwszego dysku    
              y1 - float, druga współrzędna pierwszego dysku  
              x2 - float, pierwsza współrzędna drugiego dysku 
              y2 - float, druga współrzędna drugiego dysku   
   output:
   funkcja zwraca wartość logiczną True - jeśli między dyskami zachodzi kolizja
   lub False - jeśli nie zachodzi'''
  r=0.5
  o=((x1-x2)**2+(y1-y2)**2)**0.5
  return o<2*r

