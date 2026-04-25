g = int(input())
r = int(input())

if 1 <= g <= 6 and 1 <= r <= 6:
    if g == r:
        print("Correct!")
    else:
        print("Wrong!")
else:
    print("Invalid")
