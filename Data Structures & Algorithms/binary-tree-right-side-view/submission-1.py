# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        res = []
        finalres = []
        queue = []
        queue.append(root)
        res.append([root])
        while queue: 
            layer = []
            val = len(queue)
            for i in range(0, val):
                node = queue.pop(0)
                if node.left: 
                    queue.append(node.left)
                    layer.append(node.left)
                if node.right: 
                    queue.append(node.right)
                    layer.append(node.right)
            if len(layer) > 0: 
                res.append(layer)
        
        for arr in res: 
            if len(arr) > 0: 
                finalres.append(arr[-1].val)
        return finalres