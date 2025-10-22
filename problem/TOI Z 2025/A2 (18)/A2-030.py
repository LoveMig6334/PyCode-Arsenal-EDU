A = [list(map(int, input().split())) for _ in range(5)]

abnormal_row = -1
abnormal_col = -1


for r in range(5):
    row_sum = sum(A[r])
    if row_sum % 2 != 0:
        abnormal_row = r
        break


for c in range(5):
    col_sum = A[0][c] + A[1][c] + A[2][c] + A[3][c] + A[4][c]
    if col_sum % 2 != 0:
        abnormal_col = c
        break

if abnormal_row == -1 and abnormal_col == -1:
    print(-1, -1)
else:
    print(abnormal_row, abnormal_col)
