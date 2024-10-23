# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        from collections import defaultdict
        
        d = defaultdict(int)
        
        def search(curr: TreeNode, head: Optional[TreeNode] = None, depth: int = 0):
            if curr == None:
                return
            
            left, right = curr.left, curr.right
            
            if depth:
                d[(depth, head)] += curr.val
            
            search(curr = left, head = curr, depth = depth + 1)
            search(curr = right, head = curr, depth = depth + 1)
            
        def get_node_sum(d: dict[tuple[int, int], int]):
            node_sum = defaultdict(lambda: defaultdict(int))
            for (depth, head), val in d.items():
                node_sum[depth]['g'] += val
                node_sum[depth][head] += val
            return node_sum
            
        def get_sum(depth: int, head: Optional[TreeNode] = None):
            sum_by_depth = node_sum[depth]['g']
            sum_by_head = node_sum[depth][head]
            return sum_by_depth - sum_by_head
        
        def set_modified_root(curr: TreeNode, head: Optional[TreeNode]= None, depth: int = 0) -> Optional[TreeNode]:
            if not curr:
                return
            
            node = TreeNode()
            node.val = get_sum(depth = depth, head = head)
            
            left, right = curr.left, curr.right
            
            node.left = set_modified_root(curr = left, head = curr, depth = depth + 1)
            node.right = set_modified_root(curr = right, head = curr, depth = depth + 1)
            return node
            
            
        def get_modified_root():
            node_tree = set_modified_root(curr = root, head = None, depth = 0)
            return node_tree
        
        
        search(root)
        node_sum = get_node_sum(d = d)
        return get_modified_root()