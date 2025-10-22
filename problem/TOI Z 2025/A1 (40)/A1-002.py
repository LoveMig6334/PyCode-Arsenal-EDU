money: int = int(input(""))

for i in (10, 5, 2, 1):
    print(f"{i} = {money // i}")
    money %= i
