odd = 0
even = 0

for _ in range(3):
    number = int(input())

    if number % 2 == 0:
        even += 1
    else:
        odd += 1

print(f"even {even}\nodd {odd}")
