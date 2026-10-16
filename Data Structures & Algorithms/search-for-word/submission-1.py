class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # preform dfs 
        # during a singular pathfinding run u need to keep track of visiting and such 
        # if string found wow amazing 
        # if string not found, and path is over/exhausted we need to remove all nodes from visiting 
        # keep track of current string during each dfs call 

        visited = set()
        def dfs(i, j, toSearch) -> bool:
            if len(toSearch) == 0:
                return True
            if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]):
                return False
            if (i, j) in visited:
                return False
            if toSearch[0] != board[i][j]:
                return False
            # valid char, do dfs 
            visited.add((i, j))
            res = dfs(i+1, j, toSearch[1:]) or dfs(i-1, j, toSearch[1:]) or dfs(i, j+1, toSearch[1:]) or dfs(i, j-1, toSearch[1:]) 
            if res:
                return True
            visited.remove((i, j))

        # do dfs starting from word[0]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if dfs(i, j, word):
                        return True
        return False
