class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()
        for row in range(9):
            for col in range(9):
                val = board[row][col]
                if val != '.':
                    row_key = (row, val)
                    col_key = (val, col)
                    box_key = (row // 3, col // 3, val)
                    if row_key in seen or col_key in seen or box_key in seen:
                        return False
                    seen.add(row_key)
                    seen.add(col_key)
                    seen.add(box_key)
        return True
