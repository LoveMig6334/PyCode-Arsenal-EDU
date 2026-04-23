usage = int(input())

if usage > 200:
    total = 2030 + (usage - 200) * 15
elif usage > 100:
    total = 830 + (usage - 100) * 12
elif usage > 50:
    total = 330 + (usage - 50) * 10
elif usage > 10:
    total = 50 + (usage - 10) * 7
else:
    total = usage * 5

FT = 0.5 * usage
VAT = 0.07 * total

print(f"{(total + FT + VAT):.2f}")
