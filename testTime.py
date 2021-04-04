import datetime

a=datetime.timedelta(days=1, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)
b=datetime.datetime.now()
c=datetime.timedelta(days=10)

print(b-a<b+c)