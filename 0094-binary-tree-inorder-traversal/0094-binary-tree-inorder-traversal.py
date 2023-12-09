# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def travelInorder(self, root: Optional[TreeNode], answer) -> None:
        if root.left:
            self.travelInorder(root.left, answer)
        
        answer.append(root.val)
        
        if root.right:
            self.travelInorder(root.right, answer)
        
    
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        answer = []
        
        if root:
            self.travelInorder(root, answer)
            
        return answer