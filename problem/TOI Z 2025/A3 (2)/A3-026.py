N, M = map(int, input().split())

first_pic = [input() for _ in range(N)]
sec_pic = [input() for _ in range(N)]

combo_map = {
    ("-", "-"): "-",
    ("-", "+"): "+",
    ("+", "-"): "+",
    ("-", "x"): "x",
    ("x", "-"): "x",
    ("+", "x"): "*",
    ("x", "+"): "*",
}

result = [
    "".join(combo_map[(first_pic[i][j], sec_pic[i][j])] for j in range(M))
    for i in range(N)
]

for row in result:
    print(row)
