# class Solution:
#     def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
#         maxArea = 0
#         visited = []
#         n = len(grid)
#         m = len(grid[0])
#         def dfs(i: int, j: int) -> int: 
#             if i < 0 or i >= n or j < 0 or j >= m: 
#                 return 0
#             if grid[i][j] == 0: 
#                 return 0
#             if [i, j] in visited: 
#                 return 0
#             visited.append([i, j])
#             sum = 1
#             sum += dfs(i + 1, j)
#             sum += dfs(i - 1, j)
#             sum += dfs(i, j + 1)
#             sum += dfs(i, j - 1)
#             return sum 
#         for i in range(n):
#             for j in range(m):
#                 if grid[i][j] == 1: 
#                     maxArea = max(maxArea, dfs(i, j))
#         return maxArea

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()

        def dfs(r, c):
            if (r < 0 or r == ROWS or c < 0 or
                c == COLS or grid[r][c] == 0 or
                (r, c) in visit
            ):
                return 0
            visit.add((r, c))
            return (1 + dfs(r + 1, c) +
                        dfs(r - 1, c) +
                        dfs(r, c + 1) +
                        dfs(r, c - 1))

        area = 0
        for r in range(ROWS):
            for c in range(COLS):
                area = max(area, dfs(r, c))
        return area

