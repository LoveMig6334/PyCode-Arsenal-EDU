year_range = {
    (22, 12, 19, 1): "capricorn",
    (20, 1, 18, 2): "aquarius",
    (19, 2, 20, 3): "pisces",
    (21, 3, 19, 4): "aries",
    (20, 4, 20, 5): "taurus",
    (21, 5, 20, 6): "gemini",
    (21, 6, 22, 7): "cancer",
    (23, 7, 22, 8): "leo",
    (23, 8, 22, 9): "virgo",
    (23, 9, 22, 10): "libra",
    (23, 10, 21, 11): "scorpio",
    (22, 11, 21, 12): "sagittarius",
}


def get_zodiac_sign(day, month):
    for (start_day, start_month, end_day, end_month), sign in year_range.items():
        if (month == start_month and day >= start_day) or (
            month == end_month and day <= end_day
        ):
            return sign
    return None


def main() -> None:
    day = int(input())
    month = int(input())

    print(get_zodiac_sign(day, month))


if __name__ == "__main__":
    main()
