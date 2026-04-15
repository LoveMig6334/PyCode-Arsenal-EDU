match_dict = {
    1: 100,
    2: 120,
    3: 200,
    4: 60,
}

total_cal = 0
while True:
    n = int(input())

    if n == 5:
        print("Bye Bye")
        break
    else:
        total_cal += match_dict[n]

print(f"Total Calories: {total_cal}")
