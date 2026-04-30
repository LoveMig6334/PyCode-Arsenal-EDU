start, end = map(int, input().split())
prime_list = []

for number in range(start, end + 1):
    for divisor in range(2, number):
        if number % divisor == 0:
            break
    else:
        prime_list.append(number)

if 1 in prime_list:
    prime_list.remove(1)

print(*prime_list)
print(f"Total primes: {len(prime_list)}")
