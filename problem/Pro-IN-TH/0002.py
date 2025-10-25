def min_max_1() -> None:
    n = int(input())

    number_lst = []
    for i in range(n):
        number_lst.append(int(input()))

    print(min(number_lst))
    print(max(number_lst))


def min_max_2() -> None:
    n = int(input())

    min = None
    max = None
    for i in range(n):
        number = int(input())

        if i == 0:
            min = number
            max = number
        else:
            if number < min:
                min = number
            if number > max:
                max = number
    print(min)
    print(max)


if __name__ == "__main__":
    min_max_2()
