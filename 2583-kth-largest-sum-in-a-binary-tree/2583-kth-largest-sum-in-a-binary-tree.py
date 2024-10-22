# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        from collections import defaultdict
        
        d = defaultdict(int)
        
        def search(curr: TreeNode, height = 0):
            if not curr:
                return
            
            left = curr.left
            right = curr.right
            
            d[height] += curr.val
            
            search(left, height + 1)
            search(right, height + 1)
        
        search(root)
    
        q  = [(val, key) for key, val in d.items()]
        q.sort(reverse = True)
        if k > len(q): return -1
        return q[k-1][0]
