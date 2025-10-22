month = int(input())
day = int(input())

seasons = ["winter", "spring", "summer", "fall"]
leap_seasons = ["spring", "summer", "fall", "winter"]

season_index = (month - 1) // 3

if month % 3 == 0 and day >= 21:
    print(leap_seasons[season_index])
else:
    print(seasons[season_index])
