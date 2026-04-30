start, end = map(str, input().split())
number = int(input())


map_dict = {
    ("BKK", "CNX"): (10, 30),
    ("CNX", "UBP"): (15, 40),
    ("UBP", "BKK"): (20, 40),
    ("BKK", "PKT"): (25, 50),
    ("PKT", "CNX"): (30, 60),
    ("UBP", "PKT"): (40, 70),
}

try:
    print(map_dict[(start, end)][0] + number * map_dict[(start, end)][1])
except KeyError:
    print("Error")
