N, M = map(int, input().split())

water_map = [input().split() for _ in range(N)]
result = [["-" for _ in range(M)] for _ in range(N)]


for j in range(M):
    if water_map[0][j] == "*":
        result[0][j] = "*"
    else:
        result[0][j] = "-"


for i in range(1, N):
    for j in range(M):
        if water_map[i][j] == "*" or water_map[i - 1][j] == "*":
            result[i][j] = "*"
        else:
            result[i][j] = "-"

for i in range(N):
    print(" ".join(result[i]))
