class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pac, atl = [], []
        pacSeen, atlSeen = set(), set()
        #add to set 
        n = len(heights)
        m = len(heights[0])

        #pacfic - add top row and left column without repeating corner
        for i in range(m): #adding the row
            pac.append((0, i))
            pacSeen.add((0, i))
        for i in range(1, n): #adding the col
            pac.append((i, 0))
            pacSeen.add((i, 0))

        #atlantic - add bottom row and right column without repeating corner
        for i in range(m): #adding the row
            atl.append((n-1, i))
            atlSeen.add((n-1, i))
        for i in range(0, n-1): #adding the col
            atl.append((i, m-1))
            atlSeen.add((i, m-1))

        #PREFORM BFS 
        #the reason why we do BFS is that it is a lvl by lvl search
        #doing DFS also suffices; its just we explore one path fully instead 
        def bfs(ocean, seen):
            while ocean:
                node = ocean.pop(0) #pop first element 
                #directions 
                d = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                for direction in d:
                    r, c = direction[0], direction[1]
                    r+=node[0]
                    c+=node[1]
                    if 0 <= r < n and 0 <= c < m and (r, c) not in seen and heights[r][c] >= heights[node[0]][node[1]]:
                        ocean.append((r, c))
                        seen.add((r, c))
        #now, we call BFS twice on both oceans
        bfs(pac, pacSeen)
        bfs(atl, atlSeen)
        #we take intersection of both sets at end
        inter = pacSeen.intersection(atlSeen)
        return [list(tup) for tup in inter]


        