def rotate_matrix(matrix):
    return [list(row)[::-1] for row in zip(*matrix)]
