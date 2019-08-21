def zero_matrix(matrix: list):
    r_flags = set()
    c_flags = set()
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            if matrix[r][c] == 0:
                r_flags.add(r)
                c_flags.add(c)

    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            if r in r_flags or c in c_flags:
                matrix[r][c] = 0

    print(matrix)


if __name__ == '__main__':
    matrix = [[1, 2, 3, 0],
              [1, 2, 4, 5],
              [1, 0, 2, 4]]
    zero_matrix(matrix)

    # [[0, 0, 0, 0],
    # [1, 0, 4, 0],
    # [0, 0, 0, 0]]
