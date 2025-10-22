from multiprocessing import Pool
from time import perf_counter

import matplotlib.pyplot as plt


def calculation(num: float) -> float:
    return (num * num) / 2


def main_map(range: list) -> None:
    numbers_range = range
    start_time = perf_counter()

    with Pool() as pool:
        pool.map(calculation, numbers_range)

    return perf_counter() - start_time


def main_imap(range: list) -> None:
    numbers_range = range
    start_time = perf_counter()

    with Pool() as pool:
        pool.imap(calculation, numbers_range)

    return perf_counter() - start_time


def main_unsorted(range: list) -> None:
    numbers_range = range
    start_time = perf_counter()

    with Pool() as pool:
        pool.imap_unordered(calculation, numbers_range)

    return perf_counter() - start_time


def main_gpt(range: list) -> None:
    numbers_range = range
    start_time = perf_counter()

    with Pool() as pool:
        pool.map(calculation, numbers_range)
        pool.close()
        pool.join()

    return perf_counter() - start_time


if __name__ == "__main__":
    rangesd = list(range(1, 10000000))

    res = "{:,}".format(rangesd[-1] + 1)
    print(f"Compare Time used by pool function from 1 to {res}")

    print(f"Time taken by map: {main_map(rangesd):.4f} seconds")
    print(f"Time taken by imap: {main_imap(rangesd):.4f} seconds")
    print(f"Time taken by imap unordered: {main_unsorted(rangesd):.4f} seconds")
    print(f"Time taken by gpt: {main_gpt(rangesd):.4f} seconds")

    # plot the results

    plt.figure(figsize=(10, 5))
    plt.bar(
        ["map", "imap", "imap unordered", "gpt"],
        [
            main_map(rangesd),
            main_imap(rangesd),
            main_unsorted(rangesd),
            main_gpt(rangesd),
        ],
    )
    plt.xlabel("Method")
    plt.ylabel("Time (seconds)")
    plt.title("Comparison of Pool Methods")
    plt.show()
