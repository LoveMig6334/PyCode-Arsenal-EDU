N = int(input())
M = N


matrin1 = []
for i in range(M):
    row = input().split()
    matrin1.append(row)


matrin2 = []
for i in range(M):
    row = input().split()
    matrin2.append(row)


for i in range(M):
    for j in range(M):
        print("{}".format(int(matrin1[i][j]) + int(matrin2[i][j])), end=" ")

    print()
