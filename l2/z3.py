word='alfabetadeltagamma'
index=int(input('od którego miejsca szukać?\n'))-1
print (word.find('a',index)+1)

#jeśli chcemy szukać w pętliwszystkich pozostałych a to zamiast drugiego printa:
#while (index<len(word) and word.find('a',index)!=-1):
#    print (word.find('a',index)+1), end=' '
#    index =word.find('a',index)+1
    
