# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        def popLeft(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[int]:
            
            if not list1:
                return False
            
            if not list2:
                return True
            
            if list1.val < list2.val:
                return True
            
            return False 
                
            
        if not list1 and not list2:
            return list1
        
        answer = ListNode()
        curr = answer
        while True:
            if popLeft(list1, list2):
                value = list1.val
                list1 = list1.next
            else:
                value = list2.val
                list2 = list2.next
            curr.val = value
            if not list1 and not list2:
                break
            curr.next = ListNode()
            curr = curr.next
        return answer