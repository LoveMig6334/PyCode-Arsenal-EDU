char_acl, number_acl = input().split()
char, number = input().split()

if char_acl == char:
    if number_acl == number:
        print(1_000_000)
    elif number_acl[-3:] == number[-3:]:
        print(2_000)
    elif number_acl[-2:] == number[-2:]:
        print(1_000)
    else:
        print(20)
elif char_acl != char:
    if number_acl == number:
        print(100_000)
    elif number_acl[-3:] == number[-3:]:
        print(200)
    elif number_acl[-2:] == number[-2:]:
        print(100)
    else:
        print(0)
else:
    print(0)
