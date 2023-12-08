# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def union_string(self, resultLeft: str, resultRight: str) -> str:
        if resultLeft == '' and resultRight == '':
            return ''
        
        if resultLeft and resultRight:
            return f'({resultLeft})({resultRight})'
        
        if resultLeft:
            return f'({resultLeft})'
        
        return f'()({resultRight})'
    
    
    def tree2str(self, root: Optional[TreeNode]) -> str:
        answer = str(root.val)
        resultLeft, resultRight = '', ''
        
        if root.left:
            resultLeft = self.tree2str(root.left)
        
        if root.right:
            resultRight = self.tree2str(root.right)
        
        answer += self.union_string(resultLeft, resultRight)
        
        return answer