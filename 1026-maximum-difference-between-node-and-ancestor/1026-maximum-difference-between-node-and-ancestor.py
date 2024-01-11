# Definition for a binary tree node.

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        answer = 0 
        
        def recursive(curr):
            nonlocal answer 
            if curr == None:
                return None, None
            if curr.left == None and curr.right == None:
                return curr.val, curr.val
            
            leftmin, leftmax = recursive(curr.left)
            rightmin, rightmax = recursive(curr.right)
            if leftmin == None:
                leftmin = curr.val
                leftmax = curr.val
            if rightmin == None:
                rightmin = curr.val
                rightmax = curr.val
            diff_lm = abs(curr.val - leftmin) 
            diff_rm = abs(curr.val - rightmin)
            diff_lM = abs(curr.val - leftmax) 
            diff_rM = abs(curr.val - rightmax)
            # print(curr.val, leftmin)
            # print(curr.val, rightmin)
            # print(curr.val, leftmax)
            # print(curr.val, rightmax)
            diff_max = max([diff_lm, diff_rm, diff_lM, diff_rM])
            # print(curr.val, diff_max)
            # print(curr.val, diff_max)
            answer = max(answer, diff_max)
            return min([leftmin, rightmin, curr.val]), max([leftmax, rightmax, curr.val])
        recursive(root)
        return answer