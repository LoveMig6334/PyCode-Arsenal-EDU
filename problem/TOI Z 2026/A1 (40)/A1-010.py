age = int(input())
status = input().lower()

if age < 18 or status == "s":
    print("20")
else:
    print("50")
