# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right



class Solution:
    def unionString(self, leftResult:Optional[str], rightResult:Optional[str]) -> str:
        if leftResult and rightResult:
            return f'({leftResult})({rightResult})'
        
        if leftResult:
            return f'({leftResult})'
        
        if rightResult:
            return f'()({rightResult})'
        
        return ''
        
        
    def tree2str(self, root: Optional[TreeNode]) -> str:
        answer = str(root.val)
        leftResult, rightResult = None, None
        
        if root.left:
            leftResult = self.tree2str(root.left)
            
        if root.right:
            rightResult = self.tree2str(root.right)
        
        stringResult = self.unionString(leftResult, rightResult)
        
        return answer + stringResult