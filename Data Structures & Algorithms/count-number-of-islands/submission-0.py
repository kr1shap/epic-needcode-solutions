class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        visited = [[0 for i in range(m)] for j in range(n)]
        distances = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def dfs(i: int, j: int) -> None: 
            if i < 0 or i >= n or j < 0 or j >= m: 
                return 
            if grid[i][j] == '0': 
                return
            if visited[i][j] == 1: 
                return 
            visited[i][j] = 1
            for dist in distances: 
                dfs(i + dist[0], j + dist[1])
        
        count = 0
        for i in range(n):
            for j in range(m):
                if visited[i][j] == 0 and grid[i][j] == '1': 
                    count+= 1
                    dfs(i, j)
        return count
            
            