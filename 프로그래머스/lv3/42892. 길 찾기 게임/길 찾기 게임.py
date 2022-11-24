import heapq
import sys
sys.setrecursionlimit(10**6)

def solution(nodeinfo):
    answer = [[]]
    q = []
    
    class Node:
        def __init__(self, num, y, x, left, right):
            self.num = num
            self.y = y
            self.x = x
            self.left = left
            self.right = right
    
        def findnode(self, node, y, x):
            if x < node.x:
                left = node.left
                if left == None:
                    return node
                else:
                    return self.findnode(left, y, x)
            else:
                right = node.right
                if right == None:
                    return node
                else:
                    return self.findnode(right, y, x)
        
        def get_nodes(self):
            if not (self.left or self.right):
                return [[self.num], [self.num]]
            forward, backward = [], []
            forward.extend([self.num])
            if self.left:
                num = self.left.get_nodes()
                forward.extend(num[0])
                backward.extend(num[1])
            if self.right:
                num = self.right.get_nodes()
                forward.extend(num[0])
                backward.extend(num[1])
            backward.extend([self.num])
            return [forward, backward]
        
        
    for ind, (x, y) in enumerate(nodeinfo, start = 1):
        heapq.heappush(q, (-y, x, ind))
        

    root = None
    while q:
        y, x, num = heapq.heappop(q)
        y *= -1
        node = Node(num, y, x, None, None)
        if not root:
            root = node
        else:
            parent = root.findnode(root, y, x)            
            if parent.x > x:
                parent.left = node
            else:
                parent.right = node
    return root.get_nodes()