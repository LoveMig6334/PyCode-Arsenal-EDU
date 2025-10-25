score_1 = int(input())
score_2 = int(input())
final_score = int(input())

total_score = score_1 + score_2 + final_score

if total_score >= 80:
    print("A")
elif total_score >= 75:
    print("B+")
elif total_score >= 70:
    print("B")
elif total_score >= 65:
    print("C+")
elif total_score >= 60:
    print("C")
elif total_score >= 55:
    print("D+")
elif total_score >= 50:
    print("D")
else:
    print("F")
