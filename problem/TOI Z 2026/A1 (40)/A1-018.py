def roman_number(number: int) -> str:
    if number < 0:
        return "Error : Please input positive number"

    if number not in range(1, 10):
        return "Error : Out of range"

    r_dict = {
        1: "I",
        2: "II",
        3: "III",
        4: "IV",
        5: "V",
        6: "VI",
        7: "VII",
        8: "VIII",
        9: "IX",
    }

    return r_dict[number]


if __name__ == "__main__":
    number = int(input())
    print(roman_number(number))
