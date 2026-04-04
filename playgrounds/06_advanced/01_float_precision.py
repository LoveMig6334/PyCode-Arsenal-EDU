from decimal import Decimal


def add_float_1(*arrgs) -> float:
    sum_num: Decimal = Decimal("0.0")

    for decimal in arrgs:
        a = Decimal(str(decimal))
        sum_num += a

    return float(sum_num)


def add_float_2(*arrgs) -> float:
    sum_num = 0.0

    for decimal in arrgs:
        sum_num += decimal

    return sum_num


a = [1, 2, 3]
print(add_float_1(1.1, 2.2, 3.3))
print(add_float_1(1.1, 2.2, 3.3, 4.4))
print(add_float_1(0.1, 0.2))
print(add_float_2(0.1, 0.2))
