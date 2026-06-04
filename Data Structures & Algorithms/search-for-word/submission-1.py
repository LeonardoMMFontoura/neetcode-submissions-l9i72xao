class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        directions = [(1,0),(0,1),(-1,0),(0,-1)]

        def dfs(r, c, depth):
            if len(word) == depth:
                return True
            if not (0 <= r < rows and 0 <= c < cols and board[r][c] == word[depth]):
                return False 
            temp = board[r][c]
            board[r][c] = "*"
            for dr, dc in directions:
                nr, nc = dr + r, dc + c
                if dfs(nr,nc, depth + 1):
                    return True
            board[r][c] = temp
            return False
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == word[0]:
                    if dfs(row,col, 0):
                        return True
        return False


            