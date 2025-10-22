import datetime

y1 = input()
m1 = input()
d1 = input()

date1 = datetime.date(int(y1), int(m1), int(d1))

y2 = input()
m2 = input()
d2 = input()

date2 = datetime.date(int(y2), int(m2), int(d2))

if date1 > date2:
    print("2")
elif date1 == date2:
    print("0")
else:
    print("1")
