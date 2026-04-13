score = int(input())
bonus = int(input())
days = int(input())

t_score = None

if days <= 3:
    t_score = score + bonus
else:
    t_score = (score + bonus) * 1.5

key = None

if t_score >= 1500:
    key = 5
elif t_score >= 1000:
    key = 4
elif t_score >= 500:
    key = 3
elif t_score >= 200:
    key = 2
else:
    key = 1

spa = None

if (key == 5) and (days >= 7):
    spa = 99
elif (key == 4) and (bonus >= 300):
    spa = 88
else:
    spa = 0

print(int(t_score))
print(key)
print(spa)
