class Node:
    stack = []
    status = None
    def __init__(self, num):
        self.num = num
        self.next = None
        self.prev = None

    def move(self, num):
        if num > 0:
            for i in range(num):
                if self.next.num != None:
                    self = self.next
        else:
            for i in range(abs(num)):
                if self.prev.num != None:
                    self = self.prev
        return self
    
    def delete(self):
        ind = self.num
        Node.status[ind] = 'X'
        prev, next = self.prev, self.next
        prev.next = next
        next.prev = prev
        Node.stack.append(self)
        if next.num:
            return next
        else:
            return prev

    def restore(self):
        if not Node.stack:
            return
        node = Node.stack.pop()
        Node.status[node.num] = 'O'
        prev, next = node.prev, node.next
        prev.next = node
        node.prev = prev
        next.prev = node
        node.next = next

    
class LinkedList:
    def __init__(self, n):
        self.head = Node(None)
        self.tail = Node(None)
        self.head.next = self.tail
        self.tail.prev = self.head
        Node.status = ['O'] * n
    
    def append(self, num):
        node = Node(num)
        prev, tail = self.tail.prev, self.tail
        prev.next = node
        node.prev = prev
        tail.prev = node
        node.next = tail
    
def solution(n, k, cmds):
    linkedlist = LinkedList(n)
    for i in range(n):
        linkedlist.append(i)
    cur = linkedlist.head.next # 0 부터
    cur = cur.move(k)
    
    for cmd in cmds:
        act = cmd[0]
        if act == 'U':
            num = int(cmd[2:])
            cur = cur.move(-num)
        elif act == 'D':
            num = int(cmd[2:])
            cur = cur.move(num)
        elif act == 'C':
            cur = cur.delete()
        else:
            cur.restore()
            
    return ''.join(Node.status)
