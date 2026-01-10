score_list = []
max_score = [10, 40, 50]
pas = 0

for i in range(3):
    score_list.append(int(input()))


for i in range(len(score_list)):
    if score_list[i] >= max_score[i] / 2:
        pas += 1
    else:
        pass

if pas == 3:
    print("pass")
else:
    print("fail")
