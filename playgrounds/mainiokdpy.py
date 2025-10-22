import time


def main() -> None:
    num_list: list = list(range(100))

    for index, number in enumerate(num_list):
        if number % 2 == 0:
            print(f"{-~index}. {number} is even")
        else:
            print(f"{-~index}. {number} is odd")


if __name__ == "__main__":
    start_time = time.time()
    main()
    print(f"Time use {time.time() - start_time} s")
