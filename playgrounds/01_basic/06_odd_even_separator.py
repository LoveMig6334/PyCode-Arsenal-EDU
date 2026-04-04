def is_even(number: int) -> bool:
    return True if number % 2 == 0 else False


def main() -> None:
    even_str: str = ""
    odd_str: str = ""

    while True:
        try:
            choice = input("Enter a number (type 'exit' to quit): ")

            if choice == "exit":
                print("Exiting the program.")
                break

            if is_even(int(choice)):
                even_str += choice + " "
            else:
                odd_str += choice + " "

        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            continue

    if even_str and odd_str:
        print("Even numbers entered:", even_str)
        print("Odd numbers entered:", odd_str)
    else:
        print("No numbers were entered.")


if __name__ == "__main__":
    main()
