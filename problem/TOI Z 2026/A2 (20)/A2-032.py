n, m = map(int, input().split())
k = int(input())

grid = [[0] * m for _ in range(n)]

for _ in range(k):
    r, c = map(int, input().split())
    grid[r][c] += 1

best = 0
for r in range(n):
    for c in range(m):
        if grid[r][c] != 0:
            continue
        total = 0
        for dr in (-1, 0, 1):
            for dc in (-1, 0, 1):
                if dr == 0 and dc == 0:
                    continue
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < m:
                    total += grid[nr][nc]
        if total > best:
            best = total

print(best)
