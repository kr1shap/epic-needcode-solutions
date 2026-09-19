class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        numComponents = 0 

        #create adj list 
        hashmap = dict()
        for edge in edges: 
            if edge[0] not in hashmap: 
                hashmap[edge[0]] = []
            if edge[1] not in hashmap: 
                hashmap[edge[1]] = []
            hashmap[edge[0]].append(edge[1])
            hashmap[edge[1]].append(edge[0])
        
        visited = set()
        def dfs(i): 
            if i in visited: 
                return 
            visited.add(i)
            if i not in hashmap: 
                return 
            for neigh in hashmap[i]:
                dfs(neigh)

        for i in range(n):
            if i not in visited:
                numComponents+=1 
                dfs(i)
        return numComponents