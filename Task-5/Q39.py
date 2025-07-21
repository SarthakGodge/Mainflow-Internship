def is_valid_sudoku(board):
    def is_valid_group(group):
        nums = [x for x in group if x != '.']
        return len(nums) == len(set(nums))

    for i in range(9):
        row = board[i]
        col = [board[j][i] for j in range(9)]
        if not is_valid_group(row) or not is_valid_group(col):
            return False

    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            block = [board[x][y] for x in range(i, i+3)
                                   for y in range(j, j+3)]
            if not is_valid_group(block):
                return False

    return True
