number_lst = []
for _ in range(3):
    number_lst.append(int(input()))

if number_lst[0] < number_lst[1] and number_lst[1] < number_lst[2]:
    print("increasing")
elif number_lst[0] > number_lst[1] and number_lst[1] > number_lst[2]:
    print("decreasing")
else:
    print("neither")
