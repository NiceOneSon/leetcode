# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def travel(self, root: Optional[TreeNode], answer):
        if root.left:
            self.travel(root.left, answer)
        
        answer.append(root.val)
        
        if root.right:
            self.travel(root.right, answer)
        
    
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        answer = []
        
        if root:
            self.travel(root, answer)
            
        return answer