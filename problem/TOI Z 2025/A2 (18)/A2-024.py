race_L, point = [int(i) for i in input().split()]
rabbit_jump_len, monkey_jump_len, frog_jump_len = [int(i) for i in input().split()]

point_L_lst = []
point_P_lst = []
for i in range(point):
    point_L, point_P = [int(i) for i in input().split()]

    point_P_lst.append(point_P)
    point_L_lst.append(point_L)

rabbit_score = 0
monkey_score = 0
frog_score = 0
for i in point_L_lst:
    if i % rabbit_jump_len == 0:
        rabbit_score += point_P_lst[point_L_lst.index(i)]
    if i % monkey_jump_len == 0:
        monkey_score += point_P_lst[point_L_lst.index(i)]
    if i % frog_jump_len == 0:
        frog_score += point_P_lst[point_L_lst.index(i)]

score_dict = {
    "Rabbit": rabbit_score,
    "Monkey": monkey_score,
    "Frog": frog_score,
}

max_score = max(score_dict.values())
winners = [animal for animal, score in score_dict.items() if score == max_score]

for winner in winners:
    print(winner, score_dict[winner])
