class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #preform BFS 
        #create queue
        queue = []
        time = 0
        fresh = 0
        directions = [(-1, 0), (+1, 0), (0, +1), (0, -1)]
        #add all rotting oranges to queue
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append((i, j))
                elif grid[i][j] == 1:
                    fresh+=1

        #preform BFS
        while queue and fresh > 0:
            length = len(queue)
            for j in range(length):
                #pop rotting orange off
                indexing = queue.pop(0)
                #now preform search around the rotting orange 
                for d in directions:
                    i, j = d[0], d[1]
                    #check them all off as rotting if needed
                    i+=indexing[0]
                    j+=indexing[1]
                    if 0 <= i < len(grid) and 0 <= j < len(grid[0]):
                        #valid orange, we check if rotting
                        if grid[i][j] == 1:
                            grid[i][j] = 2
                            queue.append((i, j))
                            fresh-=1
            time+=1

        return time if fresh == 0 else -1