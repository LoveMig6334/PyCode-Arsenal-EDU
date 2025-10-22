def findmoney(money: int):
    if (money / 1000) >= 1:
        n_1000 = int(money / 1000)
        money = money - (n_1000 * 1000)
        re_1 = n_1000
    else:
        re_1 = 0

    if (money / 500) >= 1:
        n_500 = int(money / 500)
        money = money - (n_500 * 500)
        re_2 = n_500
    else:
        re_2 = 0

    if (money / 100) >= 1:
        n_100 = int(money / 100)
        money = money - (n_100 * 100)
        re_3 = n_100
    else:
        re_3 = 0

    if (money / 50) >= 1:
        n_50 = int(money / 50)
        money = money - (n_50 * 50)
        re_4 = n_50
    else:
        re_4 = 0

    if (money / 20) >= 1:
        n_20 = int(money / 20)
        money = money - (n_20 * 20)
        re_5 = n_20
    else:
        re_5 = 0
    return re_1, re_2, re_3, re_4, re_5


print(findmoney(3150))
