class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        cols = len(board[0])
        directions = [(1,0), (0,1), (0,-1), (-1,0)]

        def dfs(r,c):
            if not (0 <= r < rows and 0 <= c < cols and board[r][c] == "O"):
                return 
            board[r][c] = "*"
            for dr,dc in directions:
                nr, nc = dr + r, dc + c
                dfs(nr,nc)
            return 
    
        for i in range(rows):
            dfs(i, cols -1)
            dfs(i,0)
        
        for j in range(cols):
            dfs(0,j)
            dfs(rows-1,j) 

        for row in range(rows):
            for col in range(cols):
                if board[row][col] == 'O':
                    board[row][col] = 'X'
                elif board[row][col] == '*':
                    board[row][col] = 'O' 
    
