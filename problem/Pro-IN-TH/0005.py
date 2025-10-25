from math import sqrt

a, b = map(float, input().split())
c = sqrt(a**2 + b**2)

print(f"{c:6f}")
