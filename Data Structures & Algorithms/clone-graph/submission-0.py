"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        oldToNew = {}
        #preform DFS
        #the main idea is that when we preform DFS, we look at all paths
        #we are basically looking through all edges 
        #by traversing the edges, we can append to the adj list 

        def dfs(node):
            #we first check if our node is already made (i.e. visited)
            #if it is already visited, we can just return that node 
            #we return it as it has alr been made, we can append it 
            if node in oldToNew:
                return oldToNew[node] # we return the copy 
            #else we preform DFS, and also add it to newL
            cop = Node(node.val, [])
            oldToNew[node] = cop
            for nei in node.neighbors:
                cop.neighbors.append(dfs(nei)) 
                #we append the resulting node
            return cop
        return dfs(node)

            
