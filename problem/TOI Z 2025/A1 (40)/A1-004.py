score_10 = int(input())
score_40 = int(input())
score_50 = int(input())

if not score_10 >= 5:
    print("fail")
elif not score_40 >= 20:
    print("fail")
elif not score_50 >= 25:
    print("fail")
else:
    print("pass")
