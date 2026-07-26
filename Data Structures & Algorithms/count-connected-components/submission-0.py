class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        res = 0
        adjL = {}
        for i in range(n):
            adjL[i] = []
        for edge in edges:
            adjL[edge[0]].append(edge[1])
            adjL[edge[1]].append(edge[0])
        visited = set()
        def dfs(node, prev):
            if node in visited:
                return 
            visited.add(node)
            #preform dfs 
            for nei in adjL[node]:
                if nei == prev:
                    continue
                dfs(nei, node)
        #do dfs
        for i in range(n):
            if i not in visited:
                res+=1
                dfs(i, -1)
        return res