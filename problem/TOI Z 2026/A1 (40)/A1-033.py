loop = int(input())

counter = 0
for i in range(loop):
    char = input()

    if char.lower() in "aeiou":
        counter += 1

print(counter)
