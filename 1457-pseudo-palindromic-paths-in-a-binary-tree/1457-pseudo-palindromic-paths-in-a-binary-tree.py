# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        from collections import defaultdict
        nums = defaultdict(int)
        answer = 0
        def recursive(curr: Optional[TreeNode]):
            nonlocal nums
            if not curr:
                return 0
            
            if curr and curr.left == None and curr.right == None:
                cnt = 0
                nums[curr.val] += 1
                for i in range(1, 10):
                    if nums[i] % 2 == 1:
                        cnt += 1
                nums[curr.val] -= 1
                if cnt <= 1:
                    return 1
                return 0
            
            answer = 0
            nums[curr.val] += 1 
            answer += recursive(curr.left)
            answer += recursive(curr.right)
            nums[curr.val] -= 1 
            
            return answer
        
        return recursive(root)