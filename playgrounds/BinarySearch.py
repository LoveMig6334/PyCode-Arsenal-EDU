from random import randint
from time import perf_counter

import matplotlib.pyplot as plt


def binary_search(sorted_array: list, target: int):
    """
    Perform a binary search on a sorted list to find the index of a given number.
    Args:
        sorted_array (list): A list of sorted integers.
        target (int): The integer to search for in the list.
    Returns:
        int: The index of the number if found, otherwise -1.
    """

    L, R = 0, len(sorted_array) - 1

    while L <= R:
        M = (L + R) // 2

        if sorted_array[M] == target:
            return M
        elif sorted_array[M] < target:
            L = M + 1
        else:
            R = M - 1

    return -1


def linear_search(lst: list, num: int):
    for i in range(0, len(lst)):
        if lst[i] == num:
            return i
    return -1


def measure_execution_time(algorithm, num_list, target):
    start_time = perf_counter()
    if algorithm(num_list, target) == target:
        used_time = perf_counter() - start_time
        return used_time * 1000
    return None


linear_time, binary_time = [], []
iterations: list = list(range(100, 1000))

if __name__ == "__main__":
    for num in iterations:
        target = randint(0, num)

        linear_time.append(
            measure_execution_time(linear_search, list(range(0, num)), target)
        )
        binary_time.append(
            measure_execution_time(binary_search, list(range(0, num)), target)
        )

    plt.plot(iterations, linear_time, color="b", alpha=0.6)
    plt.plot(iterations, binary_time, color="r", alpha=0.6)
    plt.xlabel("Iterations")
    plt.ylabel("Execution Time (ms)")
    plt.show()
