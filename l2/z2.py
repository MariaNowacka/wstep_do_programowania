word='alfabetagamma'
index=0
while (index<len(word) and word.find('a',index)!=-1):
    print (word.find('a',index)+1, end=' ')
    index =word.find('a',index)+1
