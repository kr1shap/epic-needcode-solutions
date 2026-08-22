# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    visited = set()
    goodNode = 0

    def goodNodes(self, root: TreeNode) -> int:
        self.visited = set()
        self.goodNode = 0

        def dfs(root: TreeNode, maxVal: int) -> Void:
            if root is None: 
                return
            if root in self.visited: 
                return 
            if maxVal <= root.val: 
                self.goodNode += 1
                maxVal = root.val
            dfs(root.left, maxVal)
            dfs(root.right, maxVal)
            self.visited.add(root)

        dfs(root, root.val)
        return self.goodNode
        
        



            

        