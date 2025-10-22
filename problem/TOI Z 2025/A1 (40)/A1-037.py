def roman_number(number: int) -> str:
    """
    Convert an integer to a Roman numeral.

    :param number: Integer to convert (1-3999).
    :return: Roman numeral as a string.
    """
    if not (1 <= number <= 3999):
        raise ValueError("Number must be between 1 and 3999")

    roman_numerals = [
        (1000, "M"),
        (900, "CM"),
        (500, "D"),
        (400, "CD"),
        (100, "C"),
        (90, "XC"),
        (50, "L"),
        (40, "XL"),
        (10, "X"),
        (9, "IX"),
        (5, "V"),
        (4, "IV"),
        (1, "I"),
    ]

    result = []
    for value, numeral in roman_numerals:
        while number >= value:
            result.append(numeral)
            number -= value

    return "".join(result)


def main():
    while True:
        try:
            number = int(input())
            break

        except ValueError:
            continue

    print(roman_number(number))


if __name__ == "__main__":
    main()
