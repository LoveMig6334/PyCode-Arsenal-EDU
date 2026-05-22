num, query = map(int, input().split())
diff = [0] * 1442
for _ in range(num):
    s, e = map(int, input().split())
    diff[s] += 1
    diff[e + 1] -= 1

open_count = [0] * 1441
cur = 0
for i in range(1441):
    cur += diff[i]
    open_count[i] = cur

times = list(map(int, input().split()))
print(*[open_count[t] for t in times])
