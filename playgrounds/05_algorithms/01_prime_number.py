from math import isqrt
from time import perf_counter


def is_prime(num: int) -> bool:
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False

    limit = isqrt(num)
    i = 5
    while i <= limit:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6

    return True


def display_primes(n: int) -> None:
    for num in range(2, n + 1):
        if is_prime(num):
            print(num)
        else:
            print(f"{num} not prime")
            continue


while True:
    try:
        n = int(input("Enter the upper limit (n, n >= 2): "))
        if n >= 2:
            start_time = perf_counter()
            break
        else:
            print("Invalid input. Please enter a positive integer greater than 2.")
    except ValueError:
        print("Invalid input. Please enter a positive integer.")

display_primes(n)

print(f"Find prime Number from 1 to {n}")
print("Runtime:", perf_counter() - start_time, "seconds")
