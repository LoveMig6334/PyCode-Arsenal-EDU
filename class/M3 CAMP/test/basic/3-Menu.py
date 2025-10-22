def menu_1() -> None:
    r = float(input("Enter the circle radius: "))
    A = 3.14 * (r**2)

    print(f"The area of the circle is {A}\n")


def menu_2() -> None:
    wide: int = int(input("Enter the wide of the triangle: "))

    for i in range(1, wide + 1, 1):
        print("#" * i)
    for i in range(wide - 1, 0, -1):
        print("#" * i)

    print()


def menu_3() -> None:
    n = int(input("Multiplication Table: "))
    for i in range(12):
        print(n, "*", i + 1, "=", (n) * (i + 1))

    print()


def main() -> None:
    while True:
        try:
            print("1. Circle Area")
            print("2. Triangle")
            print("3. Multiplication Table")
            print("4. Exit")

            choice = int(input("Enter your choice >>> "))
            print()

            if choice == 1:
                menu_1()
            elif choice == 2:
                menu_2()
            elif choice == 3:
                menu_3()
            elif choice == 4:
                print("==== Goodbye! ====")
                break
            else:
                print("==== Invalid choice ====\n")

        except ValueError:
            print("==== Please enter a number ====\n")


if __name__ == "__main__":
    main()
