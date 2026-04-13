operation = input()

X = 0
Y = 0
for op in operation:
    if op == "N":
        Y += 1
    elif op == "S":
        Y -= 1
    elif op == "E":
        X += 1
    elif op == "W":
        X -= 1

print(f"{X} {Y} {abs(X) + abs(Y)}")
