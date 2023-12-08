# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        answer = str(root.val)
        
        resultLeft, resultRight = None, None
        
        if root.left and isinstance(root.left.val, int):
            resultLeft = self.tree2str(root.left)
        
        if root.right and isinstance(root.right.val, int):
            resultRight = self.tree2str(root.right)
             
        
        if resultLeft and resultRight:
            answer += '(' + resultLeft + ')'
            answer += '(' + resultRight + ')'
        
        elif resultLeft:
            answer += '(' + resultLeft + ')'
        
        elif resultRight:
            answer += '()'
            answer += '(' + resultRight + ')'
        
        return answer
        
