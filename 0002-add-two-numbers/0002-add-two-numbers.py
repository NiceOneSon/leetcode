# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def forward(self):
        while self.next == None:
            self = self.next
        return self

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        memory = 0
        answer = None
        while l1 != None or l2 != None or memory != 0:
            val1, val2 = 0, 0
            if l1:
                val1 = l1.val
                l1 = l1.next
            if l2:
                val2 = l2.val
                l2 = l2.next
            calc = val1 + val2 + memory
            memory = calc // 10
            calc %= 10
            
            if answer == None:
                current = ListNode(val = calc, next = None)
                answer = current
            else:
                current = answer
                while current.next != None:
                    current = current.next
                current.next = ListNode(val = calc, next = None)
            
            
        
        return answer