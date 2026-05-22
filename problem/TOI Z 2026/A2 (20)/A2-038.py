n = int(input())
fire = water = earth = 0

for _ in range(n):
    f1, w1, e1, f2, w2, e2 = map(int, input().split())
    fire += max(f1, f2)
    water += max(w1, w2)
    earth += max(e1, e2)

print(fire + water + earth)
print(fire, water, earth)
print("YES" if fire > water + earth else "NO")
