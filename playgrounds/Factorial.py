def factorial(n):
    if n == 1:
        return 1
    elif n > 0:
        return n * factorial(n - 1)


while True:
    try:
        n = int(input("Enter a positive integer: "))
        if n < 0:
            print("Error! Factorial is not defined for negative numbers.")
        else:
            break
    except ValueError:
        print("Error! Invalid input. Please enter a positive integer.")

print(factorial(n))
