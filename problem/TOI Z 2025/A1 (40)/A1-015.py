name: str = input()
sur_name: str = input()
age: str = input()

if len(name) <= 5 and len(sur_name) <= 5:
    print(name[0], age, sur_name[-1], sep="")
else:
    print(name[0:2], sur_name[-1], age[-1], sep="")
