def czyAnagram(s1,s2):
    if len(s1)!=len(s2):
         print('slowa nie są anagramami')
    else:
        for j in range (len(s1)-1):
            for i in range (j):
                if s1[i]>s1[i+1]:
                    s1[i],s1[i+1]=s1[i+1],s1[i]
                if s2[i]>s2[i+1]:
                    s2[i],s2[i+1]=s2[i+1],s2[i]
    return s1==s2


s1=list(input('podaj pierwsze slowo: ').lower())
s2=list(input('podaj drugie slowo: ').lower())
print('czy słowa są anagramami?',czyAnagram(s1,s2))

