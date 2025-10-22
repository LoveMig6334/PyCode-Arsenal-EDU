def number_swap(number_str_2_digit: str) -> str:
    return number_str_2_digit[::-1]


def main() -> None:
    number = int(input())
    reversed_number = int(number_swap(str(number)))

    operation = input()

    if operation == "+":
        sum = number + reversed_number
        print(f"{number} + {reversed_number} = {sum}")
    elif operation == "*":
        product = number * reversed_number
        print(f"{number} * {reversed_number} = {product}")


if __name__ == "__main__":
    main()
