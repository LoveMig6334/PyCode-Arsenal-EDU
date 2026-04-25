from string import ascii_lowercase

input_string = input()
shift = int(input())

result = ""

for char in input_string:
    position = ascii_lowercase.index(char)
    new_position = (position + shift) % 26

    result += ascii_lowercase[new_position]

print(result)
