def ladder():
    for i in range(1, max_hight + 1):
        for j in range(i):
            print(j + 1, end="")
        print()


while True:
    try:
        max_hight = int(input("Enter The maximum of the height: "))
        if max_hight < 10:
            break
        else:
            print("Put less than 10. Try again.")
    except ValueError:
        print("Invalid input. Please enter a positive integer less than 10.")


ladder()
