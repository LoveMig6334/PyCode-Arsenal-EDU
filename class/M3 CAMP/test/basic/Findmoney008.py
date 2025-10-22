def find_money(money: float) -> tuple:
    array: tuple = (1000, 500, 100, 50, 20)
    result: list = []

    for price in array:
        result.append(money // price)
        money %= price

    return tuple(result)


def main() -> None:
    print(find_money(1200))


if __name__ == "__main__":
    main()
