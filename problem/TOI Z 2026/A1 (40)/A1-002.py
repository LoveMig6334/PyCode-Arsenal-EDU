monney = int(input())

back_list = [10, 5, 2, 1]

for i in range(len(back_list)):
    print(f"{back_list[i]} = {monney // back_list[i]}")
    monney %= back_list[i]
