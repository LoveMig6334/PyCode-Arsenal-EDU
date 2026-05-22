seats = int(input())

while True:
    try:
        a, n = map(int, input().split())
    except EOFError:
        break

    if a < 15:
        print(-1)
        continue
    if n > seats:
        print(-2)
        continue

    if a <= 22:
        price = n * 150 * 0.8
    elif a >= 60:
        price = n * 150 * 0.5
    else:
        price = n * 150

    seats -= n
    print(f"{int(price)} {seats}")
    if seats == 0:
        break
