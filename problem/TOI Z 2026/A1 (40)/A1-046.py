item_n = int(input())
item_list = input().split()

sum = 0
even = 0

for item in item_list:
    sum += int(item)

    if int(item) % 2 == 0:
        even += 1

print(f"SUM {sum}")
print(f"EVEN {even}")
print(f"ODD {item_n - even}")
