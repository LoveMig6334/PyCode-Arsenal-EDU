rgb_1 = input().split()
rgb_2 = input().split()

result = []

for index in range(3):
    value = (int(rgb_1[index]) + int(rgb_2[index])) // 2
    result.append(str(value))

print(" ".join(result))
