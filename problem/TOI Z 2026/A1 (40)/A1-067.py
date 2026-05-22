from decimal import ROUND_HALF_UP, Decimal

member = input().strip()
n = int(input())

total = Decimal("0")

for _ in range(n):
    total += Decimal(input().strip())
if member == "Y":
    total *= Decimal("0.95")
elif total >= 500:
    total *= Decimal("0.97")
print(total.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP))
