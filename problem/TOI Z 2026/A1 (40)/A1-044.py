age, day = input().split()
age = int(age)

age_price = [(5, 0), (19, 100)]
base = next((price for age_limit, price in age_price if age < age_limit), 150)

price = base * 0.5 if day == "Wed" else base

print(int(price))
