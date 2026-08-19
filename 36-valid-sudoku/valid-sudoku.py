class Solution:
    def isValidSudoku(self, board):
        # Rows
        for row in board:
            if len(set(x for x in row if x != '.')) != len([x for x in row if x != '.']):
                return False

        # Columns
        for j in range(9):
            col = []
            for i in range(9):
                if board[i][j] != '.':
                    col.append(board[i][j])

            if len(set(col)) != len(col):
                return False

        # 3x3 boxes
        for r in range(0, 9, 3):
            for c in range(0, 9, 3):
                box = []

                for i in range(r, r + 3):
                    for j in range(c, c + 3):
                        if board[i][j] != '.':
                            box.append(board[i][j])

                if len(set(box)) != len(box):
                    return False

        return True
        