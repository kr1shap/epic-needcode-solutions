"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node == None: 
            return None
        # create an array for nodes map val -> Node
        arr = [Node() for i in range(0, 101)] # 1 to 100 

        # preform dfs on given node
        visited = set()
        def dfs(node: Optional['Node']) -> None: 
            if node is None: 
                return 
            if node in visited: 
                return 
            visited.add(node)
            arr[node.val].val = node.val
            for neigh in node.neighbors:
                arr[node.val].neighbors.append(arr[neigh.val])
                dfs(neigh)
        dfs(node)
        return arr[1]

