blow_size, soup = input().split()

try:
    toping, n = input().split()
    n = int(n)
except ValueError:
    toping = "N"
    n = 0


ramen_dict = {
    "S": {"R": 60, "T": 80},
    "M": {"R": 80, "T": 100},
    "L": {"R": 100, "T": 120},
}
toping_dict = {
    "N": 0,
    "P": 15,
    "E": 10,
}


print(ramen_dict[blow_size][soup] + toping_dict[toping] * n)
