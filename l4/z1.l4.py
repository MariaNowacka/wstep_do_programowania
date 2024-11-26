i = 0
for i in range (51):
    w=i/100*100-i
    if w!=0.0:
        print(i, w)

#przy niektórych ułamkach (np. 0.07, 0.14, 0.28, 0.29) python ma problemy z
#zapamiętaniem dokładnej wartości, i przy mnożeniu *100 widać różnice między
#wartością dokładną, a tą zapamiętana przez pythona
#0.04*100 daje 4.0 - tutaj się zgadza, dlatego wynikiem działania jest 0
#0.07*100 daje 7.000000000000001  >7
#0.14*100 daje 14.000000000000002 >14
#0.28*100 daje 28.000000000000004 >28
#0.29*100 daje 28.999999999999996 <29 - dlatego w wyniku mamy liczbę ujemną

#wynika to ze sposobu reprezentacji liczb w standardzie IEEE754, niektóre liczby
#trudniej przedstawić za pomocą sumy potęg dwójki 

