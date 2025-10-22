number_lst = [int(x) for x in input().split()]

not_same = []
for number in number_lst:
    if number not in not_same:
        not_same.append(number)


for number in not_same:
    print(number, end=" ")
