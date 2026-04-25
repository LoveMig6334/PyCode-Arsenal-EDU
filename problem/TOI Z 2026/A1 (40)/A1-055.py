item_bocket = input().split()
price = 25 * int(item_bocket[0]) + 40 * int(item_bocket[1]) + 55 * int(item_bocket[2])
sum = 0

for item in item_bocket:
    sum += int(item)

if sum >= 3:
    discount = price * 0.1
    final_price = price - discount
    print(int(final_price))
else:
    print(price)
