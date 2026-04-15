car_year: int = int(input())
car_cc = int(input())


def calculate_tax(car_gen: int, car_cc: int) -> int:
    if car_gen == 1:
        if car_cc <= 1500:
            return 1250
        elif car_cc <= 2000:
            return 1400
        else:
            return 2000
    elif car_gen == 2:
        if car_cc <= 1500:
            return 1100
        elif car_cc <= 2000:
            return 1300
        else:
            return 1700
    elif car_gen == 3:
        if car_cc <= 1500:
            return 1000
        elif car_cc <= 2000:
            return 1200
        else:
            return 1500
    else:
        return 0


if car_year <= 1990:
    gen = 1
    print(calculate_tax(gen, car_cc))
elif car_year < 2000:
    gen = 2
    print(calculate_tax(gen, car_cc))
else:
    gen = 3
    print(calculate_tax(gen, car_cc))
