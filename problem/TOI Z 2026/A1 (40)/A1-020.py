number_lst = []

for i in range(3):
    number_lst.append(int(input()))


def is_sorted(lst: list) -> str:
    if lst[0] < lst[1] < lst[2]:
        return "increasing"
    elif lst[0] > lst[1] > lst[2]:
        return "decreasing"
    else:
        return "neither"


if __name__ == "__main__":
    print(is_sorted(number_lst))
