# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        def recursive(curr):
            if not curr:
                return None
            if curr.left == None and curr.right == None:
                return curr.val
            
            answer = []
            
            left = recursive(curr.left)
            if left:
                if type(left) == list:
                    answer.extend(left)
                else:
                    answer.extend([left])
            
            right = recursive(curr.right)
            if right:
                if type(right) == list:
                    answer.extend(right)
                else:
                    answer.extend([right])
            
            return answer
        
        answer1 = recursive(root1)
        answer2 = recursive(root2)
        
        return answer1 == answer2