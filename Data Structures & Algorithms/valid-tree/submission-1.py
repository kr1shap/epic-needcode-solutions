class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #we will preform dfs starting from a node
        #in preforming DFS, we navigate ALL paths 
        #we check if a certain node has already been visited
        #if so, we have a cycle 
        #if we had a tree, there would be no cyclic defn and we would not have to worry 
        #we have to be careful though, in the sense it is undirected
        #thus, this means that an edge is bidirectional; this is NOT cyclic!!!!
        #we must keep trach of the predecessor (parent) and ensure we do not explore that part agian 

        if len(edges) > n-1:
            return False #property of trees
        #1 We create a adj list, easy to form
        adjL = {} #dictionary maps a node j -> List[int] of edges
        visited = set()
        
        #create the adj list 
        for edge in edges:
            if edge[0] not in adjL:
                adjL[edge[0]] = []
            if edge[1] not in adjL:
                adjL[edge[1]] = []
            adjL[edge[0]].append(edge[1])
            adjL[edge[1]].append(edge[0])
        #check if all nodes in adjList
        for i in range(n):
            if i not in adjL:
                adjL[i] = []

        #now, create the DFS algorithm 
        def dfs(i, prev):
            if i in visited:
                return False #invalid tree
            visited.add(i)
            #else, we continue
            for edge in adjL[i]:
                if edge == prev:
                    continue
                #call DFS
                if not dfs(edge, i):
                    return False #invalid tree, return early
            return True

        return dfs(0, -1) and len(visited) == n
