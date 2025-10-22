num1, num2, num3 = map(int, input().split())
price = int(input())

distance = 2 * (num1 + num2) * num3
print(distance)
print(price * distance)
