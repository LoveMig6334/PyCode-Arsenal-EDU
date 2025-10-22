n_loop: int = int(input())

number_lst: list = []
for i in range(n_loop):
    number_lst.append(int(input()))

print(min(number_lst))
