import string

cha_str = input()

cap = 0
small = 0
for char in cha_str:
    if char in string.ascii_uppercase:
        cap += 1
    else:
        small += 1

if cap == 0:
    print("All Small Letter")
elif small == 0:
    print("All Capital Letter")
else:
    print("Mix")
