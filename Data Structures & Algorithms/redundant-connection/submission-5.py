class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # make adjacency list 
        adj = dict()
        for edge in edges: 
            u = edge[0]
            v = edge[1]
            if u not in adj: 
                adj[u] = []
            if v not in adj: 
                adj[v] = []
            adj[u].append(v)
            adj[v].append(u)
        
        # iterate edges in reverse order
        # do kruskal union for mst 
        rank = [1 for i in range(0, len(edges)+1)]
        parent = [i for i in range(0, len(edges)+1)]

        def find(node: int) -> int: 
            if parent[node] != node: 
                parent[node] = find(parent[node])
            return parent[node]

        for i in range(0, len(edges)):
            edge = edges[i]
            u = edge[0]
            v = edge[1]
            parent_u = find(u)
            parent_v = find(v)
            #find parent 
            if parent_u == parent_v: 
                return [u, v]
            if rank[parent_u] == rank[parent_v]:
                parent[parent_u] = parent_v
                rank[parent_v] +=1
            elif rank[parent_u] > rank[parent_v]:
                parent[parent_v] = parent_u
            else: 
                parent[parent_u] = parent_v
        return []
