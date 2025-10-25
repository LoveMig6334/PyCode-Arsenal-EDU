def matrix_input(m, n) -> list:
    matrix = []

    for _ in range(m):
        rows = input().split()

        row_number = []
        for j in range(n):
            row_number.append(int(rows[j]))

        matrix.append(row_number)

    return matrix


def matrix_addition(m1, m2) -> list:
    result_matrix = []

    for rows in range(len(m1)):
        row_lst = []
        for number in range(len(m1[rows])):
            plus = m1[rows][number] + m2[rows][number]
            row_lst.append(plus)

        result_matrix.append(row_lst)

    return result_matrix


def main() -> None:
    m, n = map(int, input().split())
    matrix_1 = matrix_input(m, n)
    matrix_2 = matrix_input(m, n)

    result = matrix_addition(matrix_1, matrix_2)

    for row in result:
        for number in row:
            print(number, end=" ")
        print()


if __name__ == "__main__":
    main()
