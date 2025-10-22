import time
from functools import cache, lru_cache


# Without decorator (no cache)
def fibonacci_plain(n):
    if n <= 1:
        return n
    return fibonacci_plain(n - 1) + fibonacci_plain(n - 2)


# With @cache decorator
@cache
def fibonacci_cached(n):
    if n <= 1:
        return n
    return fibonacci_cached(n - 1) + fibonacci_cached(n - 2)


def test_fibonacci_timing(n):
    # Time the plain version
    print("Testing Fibonacci calculation with and without cache...", end="\n\n")
    start_plain = time.perf_counter()
    result_plain = fibonacci_plain(n)
    end_plain = time.perf_counter()
    print(
        f"[No Cache] Result: {result_plain}, Time: {end_plain - start_plain:.8f} seconds"
    )

    # Time the cached version
    start_cached = time.perf_counter()
    result_cached = fibonacci_cached(n)
    end_cached = time.perf_counter()
    print(
        f"[With Cache] Result: {result_cached}, Time: {end_cached - start_cached:.8f} seconds"
    )


# test lru cache performance
def square_plain(n):
    print(f"Calculating square of {n}...")
    time.sleep(0.1)  # Simulate an expensive operation
    return n * n


# Cached square function
@lru_cache(maxsize=16)
def square_cached(n):
    print(f"Calculating square of {n}...")
    time.sleep(0.1)  # Simulate an expensive operation
    return n * n


def test_square():
    print("Testing square calculation with and without cache...", end="\n\n")
    test_values = [5, 5, 5, 5, 5, 6, 5, 5, 5]  # Same value repeated

    # Test without cache
    start_plain = time.perf_counter()
    for val in test_values:
        print(f"[Plain] square({val}) = {square_plain(val)}")
    end_plain = time.perf_counter()
    print(f"[Plain] Total Time: {end_plain - start_plain:.4f} seconds\n")

    # Test with lru_cache
    start_cached = time.perf_counter()
    for val in test_values:
        print(f"[Cached] square({val}) = {square_cached(val)}")
    end_cached = time.perf_counter()
    print(f"[Cached] Total Time: {end_cached - start_cached:.4f} seconds")


if __name__ == "__main__":
    test_fibonacci_timing(35)
    print()
    test_square()
