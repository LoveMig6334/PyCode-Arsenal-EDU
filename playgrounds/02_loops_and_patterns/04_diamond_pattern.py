import time


def draw_diamond(rows):
    in_row = rows
    for i in range(1, in_row + 1):
        spaces = " " * (in_row - i)
        stars = "*" * (2 * i - 1)
        print(spaces + stars)

    for i in range(in_row - 1, 0, -1):
        spaces = " " * (in_row - i)
        stars = "*" * (2 * i - 1)
        print(spaces + stars)


def main() -> float:
    rows = int(input("Enter a number of rows: "))
    start_time = time.time()

    draw_diamond(rows)

    used_time = time.time() - start_time
    print(f"You entered: {rows} rows")
    return used_time


if __name__ == "__main__":
    used_time = main()
    print(f"Time used to run the code {used_time}")
