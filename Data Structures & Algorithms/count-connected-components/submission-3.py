class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        rank = [1 for _ in range(n)]
        parent = [i for i in range(n)]

        def find(i):
            if parent[i] != i: 
                parent[i] = find(parent[i])
            return parent[i]
        
        def union(i, j):
            pari = find(i)
            parj = find(j)
            if rank[pari] == rank[parj]:
                parent[parj] = pari
                rank[pari] += 1
            elif rank[pari] > rank[parj]:
                parent[parj] = pari
            else: 
                parent[pari] = parj 

        # do union with all edges
        for edge in edges: 
            i = edge[0]
            j = edge[1]
            union(i, j)

        # print(rank)
        # print(parent)
        numComponents = 0
        # iterate through all parents and note unique ones only
        for i in range(n):
            if parent[i] == i: 
                numComponents+=1
        return numComponents
         
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # numComponents = 0 

        # #create adj list 
        # hashmap = dict()
        # for edge in edges: 
        #     if edge[0] not in hashmap: 
        #         hashmap[edge[0]] = []
        #     if edge[1] not in hashmap: 
        #         hashmap[edge[1]] = []
        #     hashmap[edge[0]].append(edge[1])
        #     hashmap[edge[1]].append(edge[0])
        
        # visited = set()
        # def dfs(i): 
        #     if i in visited: 
        #         return 
        #     visited.add(i)
        #     if i not in hashmap: 
        #         return 
        #     for neigh in hashmap[i]:
        #         dfs(neigh)

        # for i in range(n):
        #     if i not in visited:
        #         numComponents+=1 
        #         dfs(i)
        # return numComponents