class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        #because it wants nearest distance, we must use BFS
        
        #we can start from a gate, and traverse to adj spots 
        #say we have two gates near a block, we select the min distance


        #get all gate in a queue
        queue = []
        visited = set()

        def addQueue(i, j):
            if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] != -1 and (i, j) not in visited:
                visited.add((i, j))
                queue.append((i, j))
    
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    queue.append((i, j))
                    visited.add((i, j))
        distance = 0

    
        #preform BFS 
        while queue:
            for _ in range(len(queue)):
                #pop off node 
                node = queue.pop(0)
                i = node[0]
                j = node[1]
                grid[i][j] = distance
                #add neighbours to list 
                addQueue(i+1, j)
                addQueue(i-1, j)
                addQueue(i, j-1)
                addQueue(i, j+1)
            distance+=1
        return 





