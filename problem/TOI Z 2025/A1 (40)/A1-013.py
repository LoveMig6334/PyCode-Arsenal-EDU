chars: str = input()
number = input()


if chars == "H" and number == "4567":
    print("safe unlocked")
elif chars == "H" and number != "4567":
    print("safe locked - change digit")
elif chars != "H" and number == "4567":
    print("safe locked - change char")
else:
    print("safe locked")
