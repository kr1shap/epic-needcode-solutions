class Solution:
    def solve(self, board: List[List[str]]) -> None:
        #preform DFS: explore all border coords and add to   
        rows, cols = len(board), len(board[0])

        #what we want to do is mark all unsurrounded regions with 'T'
        #we preform DFS (or BFS if wanted) on the border
        def dfs(i, j):
            #check if coords valid
            #we do not need a visited array in this case
            #we only preform DFS on selected coordinates. We know any connected O are uncaptured
            #We ignore X and T. Thus, marking as 'T' is our 'seen' marker 
            if 0 <= i < rows and 0 <= j < cols and board[i][j] == "O": #we only change O, NOT X
                board[i][j] = "!"
            else:
                return
            #now, we preform DFS
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j-1)
            dfs(i,j+1)
        #now we preform dfs 

        #1 on the top row
        for i in range(cols):
            dfs(0, i)
            dfs(rows-1, i)
        #2 on the cols
        for i in range(rows):
            dfs(i, 0)
            dfs(i, cols-1)
        
        #iterate through entire matrix: mark the ! back as O
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O":
                    board[i][j] = "X"
                if board[i][j] == "!":
                    board[i][j] = "O"
                
        return