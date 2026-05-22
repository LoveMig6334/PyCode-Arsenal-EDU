n = int(input())
m = int(input())

adults = (n + 1) // 2

for i in range(n):
    if i < adults:
        print(" ".join(["A"] * m))
    else:
        print(" ".join(["K"] * m))
