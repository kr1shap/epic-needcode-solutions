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

class DSU:
    def __init__(self, n):
        self.Parent = list(range(n + 1))
        self.Size = [1] * (n + 1)

    def find(self, node):
        if self.Parent[node] != node:
            self.Parent[node] = self.find(self.Parent[node])
        return self.Parent[node]

    def union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)
        if pu == pv:
            return False
        if self.Size[pu] >= self.Size[pv]:
            self.Size[pu] += self.Size[pv]
            self.Parent[pv] = pu
        else:
            self.Size[pv] += self.Size[pu]
            self.Parent[pu] = pv
        return True

    def getSize(self, node):
        par = self.find(node)
        return self.Size[par]

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        dsu = DSU(ROWS * COLS)

        def index(r, c):
            return r * COLS + c

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        area = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if (nr < 0 or nc < 0 or nr >= ROWS or
                            nc >= COLS or grid[nr][nc] == 0
                        ):
                            continue

                        dsu.union(index(r, c), index(nr, nc))

                    area = max(area, dsu.getSize(index(r, c)))

        return area

