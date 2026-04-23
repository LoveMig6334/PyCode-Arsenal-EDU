def is_palindrome(s):
    return s == s[::-1]


def main() -> None:
    password = input().strip().zfill(5)
    is_palindrome_r = is_palindrome(password)

    floor_inr = [(0, 9), (1, 10), (2, 11), (3, 12), (4, 14)]
    floor = next((f[1] for f in floor_inr if int(password[f[0]]) > 5), 13)

    d0, d1, d3, d4 = (
        int(password[0]),
        int(password[1]),
        int(password[3]),
        int(password[4]),
    )

    if is_palindrome_r:
        if (d0 + d4) > 5:
            room_num = 1
        elif (d1 * d3) > 5:
            room_num = 2
        else:
            room_num = 0
    else:
        if d4 != 0 and (d0 // d4) > 5:
            room_num = 1
        elif (d1 - d4) > 5:
            room_num = 2
        else:
            room_num = 0

    sum_pas = sum(int(digit) for digit in password)
    mul_pass = 1
    for digit in password:
        mul_pass *= int(digit)

    sec_room_num = 1 if sum_pas > 25 else 2 if mul_pass > 55 else 0

    print(f"{floor}{room_num}{sec_room_num}")


if __name__ == "__main__":
    main()
