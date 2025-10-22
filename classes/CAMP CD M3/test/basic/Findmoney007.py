def findmoney(money: int):
    n_1000 = money // 1000
    money = money % 1000

    n_500 = money // 500
    money = money % 500

    n_100 = money // 100
    money = money % 100

    n_50 = money // 50
    money = money % 50

    n_20 = money // 20
    money = money % 20

    return n_1000, n_500, n_100, n_50, n_20


print(findmoney(1200))
