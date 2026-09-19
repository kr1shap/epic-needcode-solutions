class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        visited = set()
        n = len(grid)
        m = len(grid[0])
        def dfs(i: int, j: int) -> int: 
            if i < 0 or i >= n or j < 0 or j >= m: 
                return 0
            if grid[i][j] == 0: 
                return 0
            if (i, j) in visited: 
                return 0
            visited.add((i, j))
            sum = 1
            sum += dfs(i + 1, j)
            sum += dfs(i - 1, j)
            sum += dfs(i, j + 1)
            sum += dfs(i, j - 1)
            return sum 
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1: 
                    maxArea = max(maxArea, dfs(i, j))
        return maxArea


