def factorial(n: int) -> int:
    if n == 0:
        return 1

    return n * factorial(n - 1)


def main() -> None:
    n: int = int(input())
    print(factorial(n))


if __name__ == "__main__":
    main()
