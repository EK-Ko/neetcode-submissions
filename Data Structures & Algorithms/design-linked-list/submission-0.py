class ListNode:
    def __init__(self, val = 0, next=None, prev=None):
        self.val = val
        self.prev = prev
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.head = ListNode(-1)
        self.tail = ListNode(-1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def get(self, index: int) -> int:
        if index >= self.size:
            return -1
        curr = self.head.next
        for i in range(index):
            curr = curr.next
        return curr.val
        

    def addAtHead(self, val: int) -> None:
        newNode = ListNode(val)
        newNode.next = self.head.next
        newNode.prev = self.head

        self.head.next.prev = newNode
        self.head.next = newNode
        self.size += 1
        

    def addAtTail(self, val: int) -> None:
        newNode = ListNode(val)
        newNode.prev = self.tail.prev
        newNode.next = self.tail

        self.tail.prev.next = newNode
        self.tail.prev = newNode

        self.size += 1
        

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
        newNode = ListNode(val)
        
        curr = self.head.next
        for i in range(index):
            curr = curr.next
        newNode.prev = curr.prev
        newNode.next = curr

        curr.prev.next = newNode
        curr.prev = newNode

        self.size += 1
        

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.size:
            return
        curr = self.head.next

        for i in range(index):
            curr = curr.next
        
        curr.prev.next = curr.next
        curr.next.prev = curr.prev

        self.size -= 1
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)