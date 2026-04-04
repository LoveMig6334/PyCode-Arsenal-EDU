def find_element(num: int) -> None:
    for n in range(2, num + 1):
        for x in range(2, n):
            if n % x == 0:
                print(n, "equals", x, "*", n // x)
                break
        else:
            # loop fell through without finding a factor
            print(n, "is a prime number")


def main() -> None:
    find_element(25)


if __name__ == "__main__":
    main()
