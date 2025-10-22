import numpy as np

start_range = float(input("Enter the start range of random: "))
end_range = float(input("Enter the end range of random: "))


def number_gen(start_range, end_range):
    return np.random.uniform(start_range, end_range)


print(f"Random number is {number_gen(start_range, end_range)}")
