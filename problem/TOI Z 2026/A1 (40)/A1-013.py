safe_pass = input()
safe_digit = input()

if safe_pass == "H" and safe_digit == "4567":
    print("safe unlocked")
elif safe_pass != "H" and safe_digit == "4567":
    print("safe locked - change char")
elif safe_pass == "H" and safe_digit != "4567":
    print("safe locked - change digit")
else:
    print("safe locked")
