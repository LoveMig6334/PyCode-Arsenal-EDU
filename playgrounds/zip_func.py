def basic_zip_demo():
    print("Basic zip() usage:")
    numbers = [1, 2, 3]
    letters = ["a", "b", "c"]
    for num, letter in zip(numbers, letters):
        print(f"Number: {num}, Letter: {letter}")
    print()


def advanced_zip_demo():
    # 1. Transposing a matrix
    print("Transposing a matrix with zip():")
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    transposed = list(zip(*matrix))
    for row in transposed:
        print(row)
    print()

    # 2. Unzipping a list of tuples
    print("Unzipping a list of tuples:")
    zipped = [(1, "a"), (2, "b"), (3, "c")]
    numbers, letters = zip(*zipped)
    print("Numbers:", numbers)
    print("Letters:", letters)
    print()

    # 3. Creating a dictionary with zip()
    print("Creating a dictionary with zip():")
    keys = ["name", "age", "city"]
    values = ["Alice", 30, "New York"]
    person = {key: value for key, value in zip(keys, values)}
    print("Person Dictionary:", person)
    print()

    # 4. Iterating over multiple iterables
    print("Iterating over multiple iterables:")
    names = ["Alice", "Bob", "Charlie"]
    ages = [25, 30, 35]
    cities = ["New York", "Los Angeles", "Chicago"]
    for name, age, city in zip(names, ages, cities):
        print(f"{name} is {age} years old and lives in {city}.")
    print()

    # 5. Using zip() with enumerate()
    print("Using zip() with enumerate():")
    numbers = [10, 20, 30]
    letters = ["x", "y", "z"]
    for index, (num, letter) in enumerate(zip(numbers, letters)):
        print(f"Index {index}: Number is {num}, Letter is {letter}")


if __name__ == "__main__":
    basic_zip_demo()
    advanced_zip_demo()
