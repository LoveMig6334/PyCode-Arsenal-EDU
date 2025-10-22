number: int = int(input())


def roman_number(number: int) -> str:
    return {
        0: "N",
        1: "I",
        2: "II",
        3: "III",
        4: "IV",
        5: "V",
        6: "VI",
        7: "VII",
        8: "VIII",
        9: "IX",
    }[number]


if number < 0:
    print("Error : Please input positive number")
elif number > 9 or number == 0:
    print("Error : Out of range")
else:
    print(roman_number(number))
