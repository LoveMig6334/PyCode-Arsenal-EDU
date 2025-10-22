from sys import stdin

input = stdin.readline

R, C = map(int, input().split())
r0, c0 = map(int, input().split())

N = int(input().strip())

risk = [[0] * C for _ in range(R)]
infected_positions = [tuple(map(int, input().split())) for _ in range(N)]

for ri, ci in infected_positions:
    for dr in range(-2, 3):
        for dc in range(-2, 3):
            rr = ri + dr
            cc = ci + dc

            if rr < 0 or rr >= R or cc < 0 or cc >= C:
                continue

            d = max(abs(dr), abs(dc))
            if d == 0:
                new_risk = 100
            elif d == 1:
                new_risk = 60
            elif d == 2:
                new_risk = 20
            else:
                continue

            if new_risk > risk[rr][cc]:
                risk[rr][cc] = new_risk


safe_count = 0
for r in range(R):
    for c in range(C):
        if risk[r][c] == 0:
            safe_count += 1


rabbit_risk = risk[r0][c0]

print(safe_count)
print(f"{rabbit_risk}%")
