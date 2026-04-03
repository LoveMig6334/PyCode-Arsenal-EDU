string = input()


separation_list = []
separated_string = []

for char in range(len(string)):
    if char == 0:
        separation_list.append(string[char])
    else:
        if string[char] != string[char - 1]:
            separated_string.append((separation_list))
            separation_list = []
            separation_list.append(string[char])
        elif char == len(string) - 1:
            separation_list.append(string[char])
            separated_string.append((separation_list))
        else:
            separation_list.append(string[char])


for pack in separated_string:
    print(f"{len(pack)}{pack[0]}", end="")
