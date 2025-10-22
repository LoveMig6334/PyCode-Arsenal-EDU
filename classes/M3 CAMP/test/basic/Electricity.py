def energy(unit: int):
    if unit <= 150:
        unit = unit - 5
        if unit <= 0:
            return 0
        i = 0
        while unit > 0 and i < 10:
            unit = unit - 1
            i = i + 1
        money = (unit * 20) + (i * 15)
        return money
    else:
        i = 0
        while unit > 0 and i < 50:
            unit = unit - 1
            i = i + 1
        j = 0
        while unit > 0 and j < 100:
            unit = unit - 1
            j = j + 1
        money = ((i * 10) + (j * 17.5) + (unit * 30)) * 1.15
        return money


print(energy(185))
