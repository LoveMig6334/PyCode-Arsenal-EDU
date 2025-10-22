def calmenu(menu, a, b):
    def cal_1(a):
        A = 22 / 7 * (a**2)
        return int(A)

    def cal_2(a, b):
        A = a * b
        return int(A)

    def cal_3(a, b):
        A = 0.5 * a * b
        return int(A)

    if menu == 1:
        aws = cal_1(a)
        return aws
    elif menu == 2:
        aws = cal_2(a, b)
        return aws
    elif menu == 3:
        aws = cal_3(a, b)
        return aws
    else:
        return "error please try again"
