number_lst: list = []

for _ in range(3):
    number_lst.append(int(input()))

if len(set(number_lst)) == 3:
    print("all different")
elif len(set(number_lst)) == 2:
    print("neither")
else:
    print("all the same")
