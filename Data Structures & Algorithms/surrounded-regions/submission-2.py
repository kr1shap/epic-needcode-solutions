class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # preform dfs to find cells that are connected to edge of board
        # mark them with special delimiter 
        n = len(board)
        m = len(board[0])
        # pass thru edges of arrays and find all 'O'
        edgeO = []
        for i in range(0, n):
            if board[i][0] == 'O':
                edgeO.append([i, 0])
            if board[i][m-1] == 'O':
                edgeO.append([i, m-1])
        for i in range(0, m):
            if board[0][i] == 'O':
                edgeO.append([0, i])
            if board[n-1][i] == 'O':
                edgeO.append([n-1, i])
            
        visited = set()
        def dfs(i, j) -> None:
            if i < 0 or j < 0 or i >=n or j >=m: 
                return 
            if board[i][j] == 'X':
                return 
            if (i, j) in visited: 
                return 
            visited.add((i, j))
            if board[i][j] == 'O':
                board[i][j] = '#'
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j-1)
            dfs(i, j+1)
        
        for edge in edgeO: 
            dfs(edge[0],edge[1])

        # iterate through array and mark all delimited as #
        for i in range(n):
            for j in range(m):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == '#':
                    board[i][j] = 'O'