import datetime
p=datetime.timedelta(hours=6,minutes=52)
tr=(datetime.timedelta(minutes=6,seconds=15))
ts=(datetime.timedelta(minutes=4,seconds=12))
s1=1.5
s2=4.8
s3=1
k=p+tr*(s1+s3)+ts*s2
print(k)
