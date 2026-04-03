def add(a, b) -> int:
    return a + b


def mul(a, b) -> int:
    return a * b


def main():
    number = input()
    operation = input()
    map_operation = {"+": add, "*": mul}

    result = map_operation[operation](int(number), int(number[::-1]))
    print(f"{int(number)} {operation} {int(number[::-1])} = {result}")


if __name__ == "__main__":
    main()
