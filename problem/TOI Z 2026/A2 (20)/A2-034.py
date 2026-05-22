n = int(input())

if n < 2 or n > 32768:
    print("No")
else:
    is_prime = [False, False] + [True] * (n - 1)
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    if is_prime[n]:
        print("Yes")
        print(*[i for i in range(2, n + 1) if is_prime[i]])
    else:
        print("No")
