score_lst = []
for i in range(2):
    score_lst.append(int(input()))

total_score = sum(score_lst)
if total_score >= 50:
    print(f"{total_score}\npass")
else:
    print(f"{total_score}\nfail")
