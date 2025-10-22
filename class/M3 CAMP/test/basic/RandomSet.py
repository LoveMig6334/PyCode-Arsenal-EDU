import numpy as np


def number_generated():
    while True:
        number = np.random.uniform(-0.3, 0.3)
        if not (0 <= number <= 0.1):
            return number


def set_number():
    return [number_generated() for i in range(3)]


num_1, num_2, num_3 = set_number()

print(num_1, num_2, num_3)
