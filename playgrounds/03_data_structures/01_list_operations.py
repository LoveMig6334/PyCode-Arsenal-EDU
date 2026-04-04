def display_member(n):
    for i in range(0, n):
        print(i, end=". ")
        print(my_list[i])


def Length_Get():
    print(f"This is a list length: {len(my_list)}")


def main(operation):
    if operation == "Add":
        new_member = input("What member do you want to add to this list: ")
        my_list.append(new_member)
        print(my_list)
        Length_Get()
        exit()
    elif operation == "See":
        n = int(input("Enter the length of the member you want to see: "))
        display_member(n)
        Length_Get()
        exit()


my_list = ["apple", "orange", "banana", "cherry", "carrot", "barry", "cheese"]

while True:
    try:
        operation = input("Enter the operation Type (Add, See):")
        if operation == "Add" or operation == "See":
            break
        else:
            print("Invalid input. Please enter (Add, See)")
    except ValueError:
        print("Invalid input. Please enter a positive integer.")

main(operation)
