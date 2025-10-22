def number_input(massage: str) -> int:
    while True:
        try:
            number = int(input(massage))

            if number < 0:
                print("Invalid input. Please enter a positive integer.")
                continue

            return number
        except ValueError:
            print("Invalid input. Please enter an integer.")


def main() -> None:
    odd_numbers: list = []
    even_numbers: list = []
    while True:
        number = number_input("Enter a number: ")

        if number == 0:
            break

        if number % 2 == 0:
            even_numbers.append(number)
        else:
            odd_numbers.append(number)

    print(
        f"There are {len(odd_numbers)} odd numbers: {', '.join(map(str, odd_numbers))}"
    )
    print(
        f"There are {len(even_numbers)} even numbers: {', '.join(map(str, even_numbers))}"
    )


if __name__ == "__main__":
    main()
