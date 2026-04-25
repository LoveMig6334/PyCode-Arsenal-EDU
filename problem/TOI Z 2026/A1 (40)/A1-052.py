money = int(input())

bank_in = [1000, 500, 100]
count_ls = []

if money > 20000 or money < 100:
    print("ERROR")
    exit()

for bank in bank_in:
    count = money // bank
    count_ls.append(count)
    money -= count * bank

for count in count_ls:
    if money != 0:
        print("ERROR")
        break
    else:
        if count > 0:
            print(f"{bank_in[count_ls.index(count)]} = {count}")
