season_dict = {
    (1, 2, 3): "winter",
    (4, 5, 6): "spring",
    (7, 8, 9): "summer",
    (10, 11, 12): "fall",
}

month = int(input())
day = int(input())

if day >= 21 and month in [3, 6, 9, 12]:
    special_case = True
else:
    special_case = False

for i in range(4):
    if month in list(season_dict.keys())[i]:
        if special_case is True and i < 3:
            print(list(season_dict.values())[i + 1])
        elif special_case is True and i == 3:
            print(list(season_dict.values())[0])
        else:
            print(list(season_dict.values())[i])
