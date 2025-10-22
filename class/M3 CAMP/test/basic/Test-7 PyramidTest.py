def pyramid(n: int):
    gap = int(n - 1)
    for i in range(1, n + 1):
        print(" " * gap, end="")
        print("* " * i)
        gap = int(gap - 1)


pyramid(9)
