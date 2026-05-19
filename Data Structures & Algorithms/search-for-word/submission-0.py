class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        directions = [(0,1),(0,-1), (1,0), (-1,0)]

        def dfs(r,c, index):
            if index == len(word):
                return True

            if not (0 <= r < rows and 0 <= c < cols):
                return False

            if board[r][c] != word[index]:
                return False

            temp = board[r][c]
            board[r][c] = "*"

            for dr, dc in directions: 
                nr, nc = dr + r , dc + c
                if dfs(nr, nc, index + 1):
                    return True 

            board[r][c] = temp
            return False

        for row in range(rows):
            for col in range(cols):
                if board[row][col] == word[0]:
                    if dfs(row, col, 0):
                        return True
        return False

