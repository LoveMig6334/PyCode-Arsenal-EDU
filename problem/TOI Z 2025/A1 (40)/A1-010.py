age: int = int(input())
status: str = input()

if age < 18 or status.lower() == "s":
    print("20")
else:
    print("50")
