distance = int(input())

if distance > 10:
    price = distance * 8
elif distance > 1:
    price = ((distance - 1) * 5) + 35
else:
    price = 35

print(price)
