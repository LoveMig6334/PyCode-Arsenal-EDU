key_array = input().split()
WM = 0

for index in range(len(key_array)):
    if int(key_array[index]) < 0:
        key_array.pop(index)

for key in key_array:
    if int(key) % 2 == 0:
        WM += 1

print(f"{len(key_array) - WM} {WM} {len(key_array)}")
