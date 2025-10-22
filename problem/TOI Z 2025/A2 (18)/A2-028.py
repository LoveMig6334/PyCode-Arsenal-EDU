n = int(input())
fac_1_lst = [int(i) for i in input().strip()]
fac_2_lst = [int(i) for i in input().strip()]

pair_fac = list(zip(fac_1_lst, fac_2_lst))


right_pairs = 0
wrong_pairs = 0

for tuple_pair in pair_fac:
    if sum(tuple_pair) == 9:
        right_pairs += 1
    else:
        wrong_pairs += 1

if right_pairs == n:
    print("YES")
else:
    print("NO", wrong_pairs)
