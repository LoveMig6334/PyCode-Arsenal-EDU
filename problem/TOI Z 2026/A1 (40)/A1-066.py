x, y = map(int, input().split())

total = 0
jumps = 0
step = x

while step > 0:
    total += step
    jumps += 1
    if total >= y:
        print(jumps)
        break
    step -= 2
else:
    print(-1)
