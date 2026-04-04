date_1 = []
date_2 = []

for i in range(3):
    date_1.append(input())

for i in range(3):
    date_2.append(input())


def born_first(date_1, date_2):
    if date_1[0] < date_2[0]:
        return 1
    elif date_1[0] > date_2[0]:
        return 2
    else:
        if date_1[1] < date_2[1]:
            return 1
        elif date_1[1] > date_2[1]:
            return 2
        else:
            if date_1[2] < date_2[2]:
                return 1
            elif date_1[2] > date_2[2]:
                return 2
            else:
                return 0


print(born_first(date_1, date_2))
