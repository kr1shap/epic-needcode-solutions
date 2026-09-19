class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        atlantic = set()
        pacific = set() 
        n = len(heights)
        m = len(heights[0])

        atldfs = []
        pacdfs = []
        for i in range(0, len(heights[0])):
            pacdfs.append((0,i))
            atldfs.append((n-1, i))
        for i in range(0, len(heights)):
            pacdfs.append((i, 0))
            atldfs.append((i, m-1))

        dist = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        def dfs(i, j, visited: set, parentdis: int) -> None: 
            if 0 > i or i >= n or j < 0 or j >= m: 
                return 
            if parentdis > heights[i][j]: 
                return
            if (i,j) in visited: 
                return
            visited.add((i, j))
            for dis in dist: 
                dfs(i+ dis[0], j + dis[1], visited, heights[i][j])
        
        for atl in atldfs: 
            dfs(atl[0], atl[1], atlantic, heights[atl[0]][ atl[1]])
        for pac in pacdfs: 
            dfs(pac[0], pac[1], pacific, heights[pac[0]][ pac[1]])
        res = []
        for atl in atlantic: 
            if atl in pacific: 
                res.append([atl[0],atl[1]])
        return res
        

        