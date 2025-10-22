n = int(input())

for i in range(1, n + 1):
    if i == n:
        print("0 " * n)
    elif i >= 3:
        print("0", end=" ")
        print("1 " * (i - 2), end="")
        print("0")
    else:
        print("0 " * i)
