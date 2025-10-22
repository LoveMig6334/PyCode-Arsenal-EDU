loop_time = int(input())

score_lst = []
for i in range(loop_time):
    score_lst.append(int(input()))

print(max(score_lst))

n = 0
for i in score_lst:
    if i == max(score_lst):
        n += 1

print(n)
