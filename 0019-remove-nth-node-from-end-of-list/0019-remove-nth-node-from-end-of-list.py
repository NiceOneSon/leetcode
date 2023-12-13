# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getLength(self, curr: Optional[ListNode]) -> int:
        answer = 0
        while curr:
            curr = curr.next
            answer += 1
        return answer
    
    def popFromTheNumberOfIndex(self, curr: Optional[ListNode], idx: int) -> Optional[ListNode]:
        head = curr
        
        prev, next = None, None
        
        while idx:
            prev = curr
            curr = curr.next
            if curr and curr.next:
                next = curr.next
            idx -= 1
        
        if prev == None:
            return curr.next
        
        if curr.next == None:
            prev.next = None
            return head
        
        prev.next = next
        return head
        
    
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        
        length = self.getLength(curr)
        
        idx = length - n

        curr = self.popFromTheNumberOfIndex(curr, idx)
        
        return curr