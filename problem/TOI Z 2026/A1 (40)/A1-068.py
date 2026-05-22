n = int(input())

scores = [int(x) for x in input().split()]
avg = sum(scores) / n

print(f"{avg:.1f}")
if min(scores) >= 50 and avg >= 60.0:
    print("PASS")
else:
    print("FAIL")
