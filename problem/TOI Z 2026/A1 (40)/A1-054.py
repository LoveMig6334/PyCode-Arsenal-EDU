input_role, year, income = input().split()
year = int(year)
income = int(income)

role = [("M", 1500), ("B", 1000), ("G", 500)]
common_bonus = next(
    (bonus for r in role if r[0] == input_role for bonus in [r[1]]), None
)

if input_role == "M":
    if year > 10:
        extra_bonus = income * 0.1
    elif year >= 5:
        extra_bonus = income * 0.08
    else:
        extra_bonus = income * 0.06
elif input_role == "B":
    if year > 10:
        extra_bonus = income * 0.07
    elif year >= 5:
        extra_bonus = income * 0.06
    else:
        extra_bonus = income * 0.05
elif input_role == "G":
    if year > 10:
        extra_bonus = income * 0.06
    elif year >= 5:
        extra_bonus = income * 0.05
    else:
        extra_bonus = income * 0.04
else:
    print(0)
    exit()


print(int(common_bonus + extra_bonus))
