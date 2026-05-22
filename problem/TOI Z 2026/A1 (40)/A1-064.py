data = input().split()
n = int(data[0])

score = 0
for c in data[1 : n + 1]:
    if c == "+":
        score += 10
    else:
        score -= 5
print(score)
