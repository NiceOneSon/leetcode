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
            
        def find_kth_sum(k: int):
            q = [val for val in d.values()]
            q.sort(reverse = True)
            if k > len(q):
                return -1
            return q[k-1]
        
        search(curr = root, height = 0)

        return find_kth_sum(k)
