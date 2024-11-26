tr=6.25 #min/km
ts=4.2 #min/km
czas=tr*1.5+4.8*ts+1*tr
wyjscie=6+52/60
powrot=wyjscie+czas/60
p=int(powrot)
print(p,':',int((powrot-p)*60))

