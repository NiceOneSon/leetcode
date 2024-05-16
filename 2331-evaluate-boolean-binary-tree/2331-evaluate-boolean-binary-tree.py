# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        if root.left == None and root.right == None:
            return root.val
        
        left = self.evaluateTree(root.left)
        right = self.evaluateTree(root.right)
        
        is_and = True if root.val == 3 else False
        
        if is_and:
            if left and right:
                return 1
        else:
            if left or right:
                return 1
        return 0