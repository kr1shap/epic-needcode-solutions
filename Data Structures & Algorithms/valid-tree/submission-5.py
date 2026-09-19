class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visited = set()
        visiting = set() 

        # make adj list 
        hashmap = dict()
        for edge in edges: 
            if edge[0] not in hashmap: 
                hashmap[edge[0]] = []
            if edge[1] not in hashmap: 
                hashmap[edge[1]] = []
            hashmap[edge[0]].append(edge[1])
            hashmap[edge[1]].append(edge[0])

        def dfs(i, parent):
            if i in visited: 
                return False
            if i in visiting: 
                return True
            visiting.add(i)
            neigh = hashmap[i] if i in hashmap else []
            for n in neigh: 
                if n == parent: 
                    continue
                if dfs(n, i):
                    return True
            visiting.remove(i)
            visited.add(i)
        
        if dfs(0, -1):
            return False
        return True if len(visited) == n else False
            