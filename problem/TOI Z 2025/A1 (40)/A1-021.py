year: int = int(input())


def is_leap_year(year: int) -> bool:
    if year % 4 == 0 and year % 100 != 0:
        return True
    elif year % 400 == 0:
        return True
    else:
        return False


def is_leap_year_2(year: int) -> bool:
    return True if year % 4 == 0 else False


if year < 1582:
    if is_leap_year_2(year):
        print("yes")
    else:
        print("no")
else:
    if is_leap_year(year):
        print("yes")
    else:
        print("no")
