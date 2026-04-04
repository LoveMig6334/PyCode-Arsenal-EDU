number_set = set()

for i in range(3):
    number_set.add(int(input()))

if len(number_set) == 1:
    print("all the same")
elif len(number_set) == 2:
    print("neither")
else:
    print("all different")
