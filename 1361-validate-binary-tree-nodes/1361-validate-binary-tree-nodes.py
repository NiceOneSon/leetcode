class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        from collections import defaultdict
        
        recieves = defaultdict(int)
        parent = [i for i in range(n+1)]
        def find(p):
            if p != parent[p]:
                return find(parent[p])
            return parent[p]
        
        def union(p1, p2):
            p1 = find(p1)
            p2 = find(p2)
            
            if p1 == p2:
                return False
            elif p1 < p2:
                parent[p2] = p1
            else:
                parent[p1] = p2
            return True
        
        
        for node in range(n):
            left, right = leftChild[node], rightChild[node]
            # print(left, right)
            result = True
            if left >= 0:
                # print(left)
                recieves[left] += 1
                result = union(left, node)
            
            if right >= 0:
                # print(right)
                recieves[right] += 1
                result &= union(right, node)
            
            if result == False:
                return False
            
        p = None
        # print(recieves)
        for node in range(n):
            if p == None:
                p = find(node)
            elif p != find(node):
                return False
                
            value = recieves[node]
            if value > 1:
                return False
        
        return True
                