matrix = [
    [1, 2, 3],
    [8, 6, 3],
    [4, 2, 3],
]


def sum_matrix_column(a: list[list[float]]) -> float:
    sum_column = list(zip(*a))
    sum_column = [sum(i) for i in sum_column]

    print(sum_column)


def main() -> None:
    sum_matrix_column(matrix)


if __name__ == "__main__":
    main()
