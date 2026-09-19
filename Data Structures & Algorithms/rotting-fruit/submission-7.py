class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        que = []
        fine = set()
        n = len(grid)
        m = len(grid[0])
        # add all rotting fruit to it 
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2: 
                    que.append((i, j))
                if grid[i][j] == 1: 
                    fine.add((i, j))
        if len(que) == 0: 
            if len(fine) == 0: 
                return 0
            return -1
        
        
        time = 0 
        dist = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        #each iteration of bfs = 1 min 
        while que: 
            isAdded = False
            length = len(que)
            for _ in range(length):
                tup = que.pop(0)
                for dis in dist: 
                    i = tup[0] + dis[0]
                    j = tup[1] + dis[1]
                    if i < 0 or i >= n or j < 0 or j >= m: 
                        continue
                    if grid[i][j] == 1: 
                        grid[i][j] = 2
                        fine.remove((i, j))
                        que.append((i, j))
                        isAdded = True
            if isAdded:
                time+=1
            else: 
                break
        return time if len(fine) == 0 else -1

        # [2,1,1]
        # [1,1,0]
        # [0,1,1]

        # [X,X,0]
        # [0,X,X]
        # [0,X,2]

