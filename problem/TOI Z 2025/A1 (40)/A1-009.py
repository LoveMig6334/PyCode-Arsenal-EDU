score_mid = int(input())
score_last = int(input())

total_score = score_mid + score_last
if total_score >= 50:
    print(f"{total_score}\npass")
else:
    print(f"{total_score}\nfail")
