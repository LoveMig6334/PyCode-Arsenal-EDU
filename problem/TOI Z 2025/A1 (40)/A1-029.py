text = input()

leather_count = 0

for i in text:
    if i in "aeiou":
        leather_count += 1

print(leather_count)
